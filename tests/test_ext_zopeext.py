"""
    test_ext_zopeext
    ~~~~~~~~~~~~~~~~

    Test the zopeext.
"""
import sys
import warnings

from unittest.mock import Mock

import sphinx
from sphinx.ext.autodoc.directive import DocumenterBridge, process_documenter_options
from sphinx.util.docutils import LoggingReporter

from sphinxcontrib.zopeext.autointerface import logger

import pytest


def do_autodoc(app, objtype, name, options=None):
    # Copied from sphinx/tests/test_ext_autodoc.py
    if options is None:
        options = {}
    app.env.temp_data.setdefault("docname", "index")  # set dummy docname
    doccls = app.registry.documenters[objtype]
    docoptions = process_documenter_options(doccls, app.config, options)
    state = Mock()
    state.document.settings.tab_width = 8
    bridge = DocumenterBridge(app.env, LoggingReporter(""), docoptions, 1, state)
    documenter = doccls(bridge, name)
    documenter.generate()

    return bridge.result


@pytest.mark.sphinx("html", testroot="zopeext-autointerface")
def test_interfaces(app):
    actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface")
    assert list(actual) == [
        "",
        ".. py:interface:: IMyInterface(x)",
        "   :module: target.interfaces",
        "",
        "   This is an example of an interface.",
        "",
    ]

    actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface2")
    assert list(actual) == [
        "",
        ".. py:interface:: IMyInterface2(x)",
        "   :module: target.interfaces",
        "",
        "   A refinement of the previous interface.",
        "",
    ]


@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_classes(app):
    actual = do_autodoc(app, "function", "target.interfaces.MyImplementation")
    assert list(actual) == [
        "",
        ".. py:function:: MyImplementation(x, y=3.0)",
        "   :module: target.interfaces",
        "",
        "   Example that implements :interface:`IMyInterface`",
        "",
        "   >>> a = MyImplementation(x=2.0)",
        "   >>> a.equals(2.0)",
        "   True",
        "",
    ]

    actual = do_autodoc(app, "class", "target.interfaces.MyImplementation")
    assert list(actual) == [
        "",
        ".. py:class:: MyImplementation(x, y=3.0)",
        "   :module: target.interfaces",
        "",
        "   Example that implements :interface:`IMyInterface`",
        "",
        "   >>> a = MyImplementation(x=2.0)",
        "   >>> a.equals(2.0)",
        "   True",
        "",
    ]


@pytest.mark.skipif(sphinx.version_info < (4, 1), reason="sphinx 4.1+ is required.")
@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_class_doc_from_class(app):
    options = {"members": None, "class-doc-from": "class"}
    actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface", options)
    assert list(actual) == [
        "",
        ".. py:interface:: IMyInterface(x)",
        "   :module: target.interfaces",
        "",
        "   This is an example of an interface.",
        "",
        "",
        "   .. py:attribute:: IMyInterface.x",
        "      :module: target.interfaces",
        "",
        "      A required attribute of the interface",
        "",
        "",
        "   .. py:method:: IMyInterface.equals(x)",
        "      :module: target.interfaces",
        "",
        "      A required method of the interface.",
        "",
        "      Parameters",
        "      ----------",
        "      x : float",
        "          The parameter `x`.",
        "",
        "      Notes",
        "      -----",
        "",
        "      The argument `self` is not specified as part of the interface and",
        "      should be omitted, even though it is required in the implementation.",
        "",
    ]


@pytest.mark.skipif(sphinx.version_info < (4, 1), reason="sphinx 4.1+ is required.")
@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_class_doc_from_init(app):
    options = {"members": None, "class-doc-from": "init"}
    actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface", options)
    assert list(actual) == [
        "",
        ".. py:interface:: IMyInterface(x)",
        "   :module: target.interfaces",
        "",
        "   The constructor should set the attribute `x`.",
        "",
        "   Parameters",
        "   ----------",
        "   x : float",
        "       The parameter `x`.",
        "",
        "",
        "   .. py:attribute:: IMyInterface.x",
        "      :module: target.interfaces",
        "",
        "      A required attribute of the interface",
        "",
        "",
        "   .. py:method:: IMyInterface.equals(x)",
        "      :module: target.interfaces",
        "",
        "      A required method of the interface.",
        "",
        "      Parameters",
        "      ----------",
        "      x : float",
        "          The parameter `x`.",
        "",
        "      Notes",
        "      -----",
        "",
        "      The argument `self` is not specified as part of the interface and",
        "      should be omitted, even though it is required in the implementation.",
        "",
    ]


@pytest.mark.skipif(sphinx.version_info < (4, 1), reason="sphinx 4.1+ is required.")
@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_class_doc_from_both(app):
    options = {"members": None, "class-doc-from": "both"}
    actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface", options)
    assert list(actual) == [
        "",
        ".. py:interface:: IMyInterface(x)",
        "   :module: target.interfaces",
        "",
        "   This is an example of an interface.",
        "",
        "   The constructor should set the attribute `x`.",
        "",
        "   Parameters",
        "   ----------",
        "   x : float",
        "       The parameter `x`.",
        "",
        "",
        "   .. py:attribute:: IMyInterface.x",
        "      :module: target.interfaces",
        "",
        "      A required attribute of the interface",
        "",
        "",
        "   .. py:method:: IMyInterface.equals(x)",
        "      :module: target.interfaces",
        "",
        "      A required method of the interface.",
        "",
        "      Parameters",
        "      ----------",
        "      x : float",
        "          The parameter `x`.",
        "",
        "      Notes",
        "      -----",
        "",
        "      The argument `self` is not specified as part of the interface and",
        "      should be omitted, even though it is required in the implementation.",
        "",
    ]


@pytest.mark.skipif(sys.version_info < (3, 7), reason="python 3.7+ is required.")
@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_show_inheritance_for_subclass_of_generic_type(app):
    options = {"show-inheritance": None}
    actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface2", options)
    assert list(actual) == [
        "",
        ".. py:interface:: IMyInterface2(x)",
        "   :module: target.interfaces",
        "",
        "   Bases: :class:`target.interfaces.IMyInterface`",
        "",
        "   A refinement of the previous interface.",
        "",
    ]


@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_interface_alias(app):
    def autodoc_process_docstring(*args):
        """A handler always raises an error.
        This confirms this handler is never called for class aliases.
        """
        raise

    app.connect("autodoc-process-docstring", autodoc_process_docstring)
    actual = do_autodoc(app, "interface", "target.interfaces.IAlias")

    if sphinx.version_info < (4, 3):
        assert list(actual) == [  # 4.2.0
            "",
            ".. py:attribute:: IAlias",
            "   :module: target.interfaces",
            "",
            "   alias of :obj:`target.interfaces.IMyInterface`",
        ]
    elif False and sphinx.version_info < (4, 4, 0):
        assert list(actual) == [
            "",
            ".. py:attribute:: IAlias",
            "   :module: target.interfaces",
            "",
            "   alias of :py:obj:`target.interfaces.IMyInterface`",
        ]
    elif sphinx.version_info >= (5, 0, 2):
        assert list(actual) == [
            "",
            ".. py:attribute:: IAlias",
            "   :module: target.interfaces",
            "",
            "   alias of :py:obj:`~target.interfaces.IMyInterface`"
        ]
    else:
        assert list(actual) == [
            "",
            ".. py:attribute:: IAlias",
            "   :module: target.interfaces",
            "",
            "   alias of :py:obj:`target.interfaces.IMyInterface`",
        ]

    #### To Do: Why is this not `:py:interface:`?
    [
        "",
        ".. py:attribute:: IAlias",
        "   :module: target.interfaces",
        "",
        "   alias of :py:interface:`target.interfaces.IMyInterface`",
    ]


@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_interface_alias_having_doccomment(app):
    actual = do_autodoc(app, "interface", "target.interfaces.IOtherAlias")
    if sphinx.version_info < (4, 1, 2):
        assert list(actual) == [  # 3.4.3
            "",
            ".. py:attribute:: IOtherAlias",
            "   :module: target.interfaces",
            "",
            "   Here is a doccomment for a docstring",
            "",
            "   alias of :obj:`target.interfaces.IMyInterface`",
        ]
    elif sphinx.version_info < (4, 2):
        assert list(actual) == [  # 4.1.2
            "",
            ".. py:attribute:: IOtherAlias",
            "   :module: target.interfaces",
            "",
            "   Here is a doccomment for a docstring",
            "",
        ]
    else:
        assert list(actual) == [  # 4.3.2
            "",
            ".. py:attribute:: IOtherAlias",
            "   :module: target.interfaces",
            "",
            "   Here is a doccomment for a docstring",
            "",
        ]
        # I don't know why later versions do not include the alias...


@pytest.mark.sphinx(buildername="html", testroot="zopeext-autointerface")
def test_missing_member(app):
    """Regression test for issue #3.

    A member "missing_member" is explicitly requested, but does not exist.
    """
    old_warning = logger.warning

    def warning(msg):
        old_warning(msg)
        warnings.warn(msg)

    logger.warning = warning

    options = {"members": "missing_member,x"}
    with warnings.catch_warnings(record=True) as w:
        actual = do_autodoc(app, "interface", "target.interfaces.IMyInterface", options)

    if sphinx.version_info < (3, 5):
        assert list(actual) == [
            "",
            ".. py:interface:: IMyInterface(x)",
            "   :module: target.interfaces",
            "",
            "   This is an example of an interface.",
            "",
            "",
            "   .. py:attribute:: IMyInterface.x",
            "      :module: target.interfaces",
            "",
        ]
    else:
        assert list(actual) == [
            "",
            ".. py:interface:: IMyInterface(x)",
            "   :module: target.interfaces",
            "",
            "   This is an example of an interface.",
            "",
            "",
            "   .. py:attribute:: IMyInterface.x",
            "      :module: target.interfaces",
            "",
            "      A required attribute of the interface",
            "",
        ]

    if sphinx.version_info < (7, 2):
        # Earlier versions of sphinx have some Deprecation Warnings.
        w = [w for w in w if w.category is not DeprecationWarning]
    assert len(w) == 1
    assert (
        "missing attribute missing_member in interface target.interfaces.IMyInterface"
        in str(w[0].message)
    )
