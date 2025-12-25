# -*- coding: utf-8 -*-
import sphinxcontrib.zopeext
import sys

sys.path.insert(0, ".")
import example

extensions = [
    #'sphinx.ext.autodoc',  # Should be included on setup.
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.zopeext.autointerface",
    #'repoze.sphinx.autointerface',
]

autodoc_default_options = {"member-order": "groupwise"}

master_doc = "index"

intersphinx_mapping = {
    "zope.interface": ("https://zopeinterface.readthedocs.io/en/latest/", None),
}

nitpicky = True
