<!-- Note: this file is simplified without text roles so it displays on PyPI. See
     doc/README.rst for the correct information.-->
   
zopeext for Sphinx
==================


[![Test badge][]][GitHub Tests Workflow]
[![PyPI badge][]][PyPI link]
[![gh: tag badge][]][gh: tags]
[![Coverage badge][]][Coverage link]
[![Documentation status badge][]][Documentation link]
[![Python versions badge][]][PyPI link]

<!--
[![open-ssf badge][]][open-ssf link]

[![gh: tag badge][]][gh: tags]
[![gh: forks badge][]][gh: forks]
[![gh: contributors badge][]][gh: contributors]
[![gh: stars badge][]][gh: stars]
[![gh: issues badge][]][gh: issues]
-->

[Test badge]: <https://github.com/sphinx-contrib/zopeext/actions/workflows/tests.yaml/badge.svg>
[GitHub Tests Workflow]: <https://github.com/sphinx-contrib/zopeext/actions/workflows/tests.yaml>
[PyPI badge]: <https://img.shields.io/pypi/v/sphinxcontrib-zopeext?logo=python&logoColor=FBE072">
[Coverage badge]: <https://coveralls.io/repos/github/sphinx-contrib/zopeext/badge.svg?branch=main>
[Coverage link]: <https://coveralls.io/github/sphinx-contrib/zopeext?branch=main>
[Documentation status badge]: <https://readthedocs.org/projects/zopeext/badge/?version=latest> 
[Documentation link]:  <https://zopeext.readthedocs.io/en/latest/?badge=latest>
[Python versions badge]:
  <https://img.shields.io/pypi/pyversions/sphinxcontrib-zopeext?logo=python&logoColor=FBE072>
[PyPI link]: <https://pypi.org/project/sphinxcontrib-zopeext/>
[open-ssf badge]: 
  <https://api.securityscorecards.dev/projects/github.com/sphinx-contrib/zopeext/badge>
[open-ssf link]: <https://deps.dev/pypi/sphinxcontrib-zopeext>

[gh: forks badge]: <https://img.shields.io/github/forks/sphinx-contrib/zopeext.svg?logo=github>
[gh: forks]: <https://github.com/sphinx-contrib/zopeext/network/members>
[gh: contributors badge]: 
  <https://img.shields.io/github/contributors/sphinx-contrib/zopeext.svg?logo=github>
[gh: contributors]: <https://github.com/sphinx-contrib/zopeext/graphs/contributors>
[gh: stars badge]: <https://img.shields.io/github/stars/sphinx-contrib/zopeext.svg?logo=github>
[gh: stars]: <https://github.com/sphinx-contrib/zopeext/stargazers>
[gh: tag badge]: <https://img.shields.io/github/v/tag/sphinx-contrib/zopeext?logo=github>
[gh: tags]: <https://github.com/sphinx-contrib/zopeext/tags>
[gh: issues badge]: <https://img.shields.io/github/issues/sphinx-contrib/zopeext?logo=github>
[gh: issues]: <https://github.com/sphinx-contrib/zopeext/issues>

This extension provides an `autointerface` directive for [Zope interfaces][].

Installation
============

```bash
python3 -m pip install sphinxcontrib-zopeext
python3 -m pip install sphinxcontrib-zopeext[test,doc]
```

This requires [Sphinx][] and [zope.interface][].  The second form includes the `test`
and `doc` extras needed to run the tests and/or build the documentation.

Usage
=====

In the [build configuration file][] (the `conf.py` in your [Sphinx][]
documentation directory) add `sphinxcontrib.zopeext.autointerface` to your
`extensions` list:

```python
# conf.py
...
extensions = [..., 'sphinxcontrib.zopeext.autointerface', ...]
```

Then, in your documentation, use `autointerface` as you would use `autoclass`.  You can
refer to the interface with the `:py:interface:` role `example.IMyInterface` as you
would use the `:py:class:` role to refer to the implementation
`example.MyImplementation`:

```reStructuredText
.. automodule:: example
   :show-inheritance:
   :inherited-members:
```

One can also limit which members are displayed, just as you would with `.. autoclass`:

```reStructuredText
.. autointerface:: example.IMyInterface
   :members: x, equals
.. autoclass:: example.MyImplementation
   :members: x, equals
```

[Sphinx]: <https://sphinx.pocoo.org/>
[build configuration file]: <https://sphinx.pocoo.org/config.html>
[Zope interfaces]: <https://zopeinterface.readthedocs.io/en/latest/README.html>
[zope.interface]: <https://pypi.python.org/pypi/zope.interface/>
[sphinxcontrib.zopeext]: <https://pypi.python.org/pypi/sphinxcontrib-zopeext/>
