# -*- coding: utf-8 -*-

import sphinxcontrib.zopeext

extensions = [#'sphinx.ext.autodoc',  # Should be included on setup.
              'sphinx.ext.autosummary',
              'sphinxcontrib.zopeext.autointerface',
              #'repoze.sphinx.autointerface',
]

autodoc_default_options = {
    'member-order': 'groupwise'
}

master_doc = 'index'
