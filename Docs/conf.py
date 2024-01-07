# -*- coding: utf-8 -*-
#
# sphinxcontrib-zopeext documentation build configuration file
#
# Based on conf.py from the main sphinx documentation

import os
import sys

import sphinxcontrib.zopeext

# Add current directory to path so we can import the example.py file.
sys.path.insert(0, os.path.abspath("."))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinxcontrib.zopeext.autointerface",
]

master_doc = "index"
templates_path = ["_templates"]
exclude_patterns = ["_build"]

source_suffix = ".rst"

# General information about the project.
project = "sphinxcontrib-zopeext"
author = "Michael McNeil Forbes"
copyright = "2009-2023, " + author
version = sphinxcontrib.zopeext.__version__
release = version

html_theme = "sphinxdoc"
html_theme = "sphinx_book_theme"
# html_logo = "logo.jpg"  # Needed for sidebars

modindex_common_prefix = ["sphinxcontrib.zopeext."]
html_static_path = ["_static"]

autoclass_content = "both"

# This CSS file just makes the headers of interfaces green so we can make sure they have
# the correct class
# html_css_files = ["_custom.css"]

html_use_opensearch = "http://packages.python.org/sphinxcontrib-zopeext"
htmlhelp_basename = "sphinxcontrib-zopeextdoc"

latex_documents = [
    (
        "index",
        "sphinxcontrib-zopeext.tex",
        "sphinxcontrib-zopeext Documentation",
        author,
        "manual",
        1,
    )
]

latex_elements = {
    "fontpkg": "\\usepackage{palatino}",
}
latex_show_urls = "footnote"

intersphinx_mapping = {
    "sphinx": ("http://www.sphinx-doc.org/en/master/", None),
    "zope": ("https://www.zope.org/", None),
    "zope.interface": ("https://zopeinterface.readthedocs.io/en/latest/", None),
}

nitpick = True

# Most themes have no styling for interfaces, only class, or exception.  Here is some
# javascript that adds the HTML "class" class everywhere there is an HTML "interface"
# class.  This applies "class" formatting to interfaces.
_ADD_CLASS_TO_INTERFACE = """
$(document).ready(function() {
 $('.interface').addClass('class');
});
"""
_ADD_CLASS_TO_INTERFACE = """
"""


def setup(app):
    app.add_js_file(None, body=_ADD_CLASS_TO_INTERFACE)
