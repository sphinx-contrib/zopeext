# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.abspath("."))

# import sphinxcontrib.zopeext

extensions = [
    "sphinx.ext.autosummary",
    "sphinxcontrib.zopeext.autointerface",
    #'repoze.sphinx.autointerface',
]

# The suffix of source filenames.
source_suffix = ".rst"

autodoc_default_options = {"member-order": "groupwise"}

master_doc = "index"

nitpicky = True
