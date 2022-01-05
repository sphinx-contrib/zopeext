"""
=============
autointerface
=============

This Sphinx extension adds an :rst:dir:`autointerface` directive, which can be
used like :rst:dir:`sphinx:autoclass` to document zope interfaces.  Interfaces
are intended to be very different beasts than regular python classes, and as a
result require customized access to documentation, signatures etc.

.. rst:directive:: autointerface

   The :rst:dir:`autointerface` directive has the same form and option as the
   :rst:dir:`sphinx:autoclass` directive::

       .. autointerface:: IClass
          ...

   .. seealso:: :mod:`sphinx.ext.autodoc`

   .. note:: This extension also serves as a simple example of using the sphinx
      version 0.6 :mod:`sphinx.ext.autodoc` refactoring.  Mostly this was
      straight forward, but I stumbled across one "gotcha":

      The `objtype` attribute of the documenters needs to be unique.  Thus, for
      example, :attr:`InterfaceMethodDocumenter.objtype` cannot be `'method'`
      because this would overwrite the entry in :attr:`AutoDirective._registry`
      used to choose the correct documenter.

======================
Implementation Details
======================

.. autosummary::

   interface_getattr
   interface_format_args
   InterfaceDocumenter
   InterfaceAttributeDocumenter
   InterfaceMethodDocumenter
   InterfaceDirective
   setup

"""
from typing import Any, Dict, Tuple

import sphinx.ext.autodoc
import sphinx.domains.python
import sphinx.roles
from sphinx.locale import _
from sphinx.application import Sphinx

import zope.interface.interface

from sphinx.ext.autodoc import (
    ClassDocumenter,
    ObjectMembers,
    logger,
    __,
)
from sphinx.domains.python import PyXRefRole

from . import __version__


def interface_getattr(*v):
    """Behaves like `getattr` but for zope Interface objects which
    hide the attributes.

    .. note:: Originally I simply tried to
       override :meth:`InterfaceDocumenter.special_attrgetter` to deal with the
       special access needs of :class:`Interface` objects, but found that this
       is not intended to be overwritten.  Instead one should register the
       special accessor using :func:`app.add_autodoc_attrgetter`.
    """
    obj, name = v[:2]
    if "__dict__" == name:
        # Interface objects do not list their members through
        # __dict__.
        return dict((n, obj.get(n)) for n in obj.names())

    if name in obj.names(all=True):
        return obj.get(name)
    else:
        return getattr(*v)


def interface_format_args(obj):
    """Return the signature of an interface method or of an
    interface."""
    sig = "()"
    if isinstance(obj, zope.interface.interface.InterfaceClass):
        if "__init__" in obj:
            sig = interface_format_args(obj.get("__init__"))
    else:
        sig = obj.getSignatureString()
    return sig


class InterfaceDocumenter(ClassDocumenter):
    """A Documenter for :class:`zope.interface.Interface` interfaces."""

    objtype = "interface"
    directivetype = "interface"

    # Since these have very specific tests, we give the classes defined here
    # very high priority so that they override any other documenters.
    priority = 100 + ClassDocumenter.priority

    @classmethod
    def can_document_member(
        cls, member: Any, membername: str, isattr: bool, parent: Any
    ) -> bool:
        return isinstance(member, zope.interface.interface.InterfaceClass)

    def format_args(self) -> str:
        return interface_format_args(self.object)

    def get_object_members(self, want_all: bool) -> Tuple[bool, ObjectMembers]:
        """
        Return `(members_check_module, members)` where `members` is a
        list of `(membername, member)` pairs of the members of *self.object*.

        If *want_all* is True, return all members.  Else, only return those
        members given by *self.options.members* (which may also be None).
        """
        obj = self.object
        names = sorted(obj.names(all=want_all))
        if not want_all:
            if not self.options.members:
                return False, []  # type: ignore
            # specific members given
            selected = []
            for name in self.options.members:  # type: str
                if name in names:
                    selected.append((name, obj.get(name)))
                else:
                    logger.warning(
                        __("missing attribute %s in interface %s")
                        % (name, self.fullname),
                        type="autointerface",
                    )
            return False, selected
        elif self.options.inherited_members:
            return False, [(_name, obj.get(_name)) for _name in names]
        else:
            return False, [
                (_name, obj.get(_name))
                for _name in names
                if obj.get(_name).interface == self.object
            ]

    @staticmethod
    def autodoc_process_docstring(app, what, name, obj, options, lines):
        """Hook that adds the constructor to the object so it can be found."""
        if not isinstance(obj, zope.interface.interface.InterfaceClass):
            return

        constructor = obj.get("__init__")
        if not constructor:
            return

        # A bit of a hack, but works properly.
        obj.__init__ = constructor
        return

    def add_directive_header(self, sig: str) -> None:
        show_inheritance = self.options.show_inheritance
        self.options.show_inheritance = False
        super().add_directive_header(sig)

        if show_inheritance:
            self.options.show_inheritance = True

        # add inheritance info, if wanted
        if not self.doc_as_attr and self.options.show_inheritance:
            sourcename = self.get_sourcename()
            self.add_line("", sourcename)
            bases_ = self.object.getBases()
            if bases_:
                bases = [":class:`%s.%s`" % (b.__module__, b.__name__) for b in bases_]
                self.add_line("   " + _("Bases: %s") % ", ".join(bases), sourcename)


class InterfaceAttributeDocumenter(sphinx.ext.autodoc.AttributeDocumenter):
    """A Documenter for :class:`zope.interface.interface.Attribute`
    interface attributes.
    """

    objtype = "interfaceattribute"  # Called 'autointerfaceattribute'
    directivetype = "attribute"  # Formats as a 'attribute' for now
    priority = 100 + sphinx.ext.autodoc.AttributeDocumenter.priority
    member_order = 60  # Order when 'groupwise'

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        res = isinstance(member, zope.interface.interface.Attribute) and not isinstance(
            member, zope.interface.interface.Method
        )
        return res

    def isslotsattribute(self) -> bool:
        return False

    def generate(self, *v, **kw):
        super().generate(*v, **kw)

    def add_directive_header(self, sig: str) -> None:
        # Hack to remove the value.
        self.non_data_descriptor = False
        super().add_directive_header(sig)

    def add_content(self, more_content, no_docstring=False):
        # Correct behavior of AttributeDocumenter.add_content.
        # Don't run the source analyzer... just get the documentation
        self.analyzer = None
        # Treat attributes as datadescriptors since they have docstrings
        self.non_data_descriptor = False
        super().add_content(more_content, no_docstring)


class InterfaceMethodDocumenter(sphinx.ext.autodoc.MethodDocumenter):
    """
    A Documenter for :class:`zope.interface.interface.Method`
    interface attributes.
    """

    objtype = "interfacemethod"  # Called 'autointerfacemethod'
    directivetype = "method"  # Formats as a 'method' for now
    priority = 100 + sphinx.ext.autodoc.MethodDocumenter.priority
    member_order = 70  # Order when 'groupwise'

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, zope.interface.interface.Method)

    def format_args(self):
        return interface_format_args(self.object)


class InterfaceDirective(sphinx.domains.python.PyClasslike):
    r"""An `'interface'` directive."""

    def get_index_text(self, modname, name_cls):
        if self.objtype == "interface":
            return _("%s (interface in %s)") % (name_cls[0], modname)
        else:
            return ""


# Many themes provide no styling for interfaces, so we add some javascript here that
# inserts "class" as well, so that interfaces fallback to class formatting.  (I.e. the
# HTML `class="py interface"` will become `class="py interface class"`
_JS_TO_ADD_CLASS_TO_INTERFACE = """
$(document).ready(function() {
  $('.interface').addClass('class');
});
"""


def setup(app: Sphinx) -> Dict[str, Any]:
    app.setup_extension("sphinx.ext.autodoc")
    app.add_autodoc_attrgetter(
        zope.interface.interface.InterfaceClass, interface_getattr
    )
    app.add_autodocumenter(InterfaceDocumenter)
    app.add_autodocumenter(InterfaceAttributeDocumenter)
    app.add_autodocumenter(InterfaceMethodDocumenter)

    app.add_directive_to_domain("py", "interface", InterfaceDirective)
    app.add_role_to_domain("py", "interface", PyXRefRole())
    app.connect(
        "autodoc-process-docstring", InterfaceDocumenter.autodoc_process_docstring
    )

    app.add_js_file(None, body=_JS_TO_ADD_CLASS_TO_INTERFACE)
    return {"version": __version__}
