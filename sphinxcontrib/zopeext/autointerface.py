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
import sphinx.ext.autodoc
import sphinx.domains.python
import sphinx.roles
from sphinx.locale import _

import zope.interface.interface

ALL = sphinx.ext.autodoc.ALL


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
    r"""Return the signature of an interface method or of an
    interface."""
    sig = "()"
    if isinstance(obj, zope.interface.interface.InterfaceClass):
        if '__init__' in obj:
            sig = interface_format_args(obj.get('__init__'))
    else:
        sig = obj.getSignatureString()
    return sig


class InterfaceDocumenter(sphinx.ext.autodoc.ClassDocumenter):
    """A Documenter for :class:`zope.interface.Interface` interfaces.
    """
    objtype = 'interface'               # Called 'autointerface'

    # Since these have very specific tests, we give the classes defined here
    # very high priority so that they override any other documenters.
    priority = 100 + sphinx.ext.autodoc.ClassDocumenter.priority

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, zope.interface.interface.InterfaceClass)

    def format_args(self):
        return interface_format_args(self.object)

    def get_object_members(self, want_all):
        """
        Return `(members_check_module, members)` where `members` is a
        list of `(membername, member)` pairs of the members of *self.object*.

        If *want_all* is True, return all members.  Else, only return those
        members given by *self.options.members* (which may also be None).
        """
        obj = self.object
        names = sorted(obj.names(want_all))
        members = self.options.get('members', None)
        if members and members is not ALL:
            names = [name for name in members if name in set(names)]

        # We exclude __init__ here since the arguments are rolled into the
        # class signature, and the documentation is included in the class
        # documentation.
        return False, [(_name, obj.get(_name))
                       for _name in names
                       if _name != '__init__']

    @staticmethod
    def autodoc_process_docstring(app, what, name, obj, options, lines):
        """Hook that adds the constructor docstring to the interface
        docstring."""
        if not isinstance(obj, zope.interface.interface.InterfaceClass):
            return

        constructor = obj.get('__init__')
        if not constructor:
            return

        constructor_lines = constructor.getDoc()
        if not constructor_lines:
            return

        # Docstring provided for constructor, so add it to the class docstring.
        lines.extend([""] + constructor_lines.splitlines())


class InterfaceAttributeDocumenter(sphinx.ext.autodoc.AttributeDocumenter):
    """A Documenter for :class:`zope.interface.interface.Attribute`
    interface attributes.
    """
    objtype = 'interfaceattribute'   # Called 'autointerfaceattribute'
    directivetype = 'attribute'      # Formats as a 'attribute' for now
    priority = 100 + sphinx.ext.autodoc.AttributeDocumenter.priority

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        res = (isinstance(member, zope.interface.interface.Attribute)
               and not isinstance(member, zope.interface.interface.Method))
        return res

    def add_content(self, more_content, no_docstring=False):
        # Bypass the original add_content method which filters out the content
        # for attributes since interfaces actually have documentation (whereas
        # regular attributes are values which have incorrect documentation).
        sphinx.ext.autodoc.ClassLevelDocumenter.add_content(
            self, more_content, no_docstring)


class InterfaceMethodDocumenter(sphinx.ext.autodoc.MethodDocumenter):
    """
    A Documenter for :class:`zope.interface.interface.Attribute`
    interface attributes.
    """
    objtype = 'interfacemethod'   # Called 'autointerfacemethod'
    directivetype = 'method'      # Formats as a 'method' for now
    priority = 100 + sphinx.ext.autodoc.MethodDocumenter.priority

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, zope.interface.interface.Method)

    def format_args(self):
        return interface_format_args(self.object)


class InterfaceDirective(sphinx.domains.python.PyClasslike):
    r"""An `'interface'` directive."""
    def get_index_text(self, modname, name_cls):
        if self.objtype == 'interface':
            if not modname:
                return '%s (built-in interface)' % name_cls[0]
            return '%s (%s interface)' % (name_cls[0], modname)
        else:
            return ''


def setup(app):
    app.add_autodoc_attrgetter(zope.interface.interface.InterfaceClass,
                               interface_getattr)
    app.add_autodocumenter(InterfaceDocumenter)
    app.add_autodocumenter(InterfaceAttributeDocumenter)
    app.add_autodocumenter(InterfaceMethodDocumenter)

    domain = sphinx.domains.python.PythonDomain
    domain.object_types['interface'] = sphinx.domains.python.ObjType(
        _('interface'), 'interface', 'obj')
    domain.directives['interface'] = InterfaceDirective
    domain.roles['interface'] = sphinx.domains.python.PyXRefRole()

    app.connect('autodoc-process-docstring',
                InterfaceDocumenter.autodoc_process_docstring)
