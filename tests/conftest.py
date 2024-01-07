"""
    pytest config for zopeext/tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

try:
    # importlib.metadata is present in Python 3.8 and later
    import importlib.metadata as importlib_metadata
except ImportError:
    # use the shim package importlib-metadata pre-3.8
    import importlib_metadata as importlib_metadata

import os
from pathlib import Path


import shutil

import pytest

import sphinx
    
import sphinxcontrib.zopeext

pytest_plugins = "sphinx.testing.fixtures"

# Exclude 'roots' dirs for pytest test collector
collect_ignore = ["roots"]


@pytest.fixture(scope="session")
def rootdir():
    if sphinx.version_info < (7, 2):
        from sphinx.testing.path import path
        return path(__file__).parent.abspath() / "roots"
    return Path(__file__).parent.absolute() / "roots"


def pytest_report_header(config):
    header = "libraries: Sphinx-%s, zope.interface-%s, sphinxcontrib.zopeext-%s" % (
        sphinx.__display_version__,
        importlib_metadata.version("zope.interface"),
        sphinxcontrib.zopeext.__version__,
    )
    if hasattr(config, "_tmp_path_factory"):
        header += "\nbase tempdir: %s" % config._tmp_path_factory.getbasetemp()

    return header


def _initialize_test_directory(session):
    if "SPHINX_TEST_TEMPDIR" in os.environ:
        tempdir = os.path.abspath(os.getenv("SPHINX_TEST_TEMPDIR"))
        print("Temporary files will be placed in %s." % tempdir)

        if os.path.exists(tempdir):
            shutil.rmtree(tempdir)

        os.makedirs(tempdir)


def pytest_sessionstart(session):
    _initialize_test_directory(session)
