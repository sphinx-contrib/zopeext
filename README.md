<!-- Note: this file is simplified without text roles so it displays on PyPI. See
     doc/README.rst for the correct information.-->
   
zopeext for Sphinx
==================

[![Test badge][]][GitHub Tests Workflow]

[Test badge]: <https://github.com/sphinx-contrib/zopeext/actions/workflows/tests.yaml/badge.svg>
[GitHub Tests Workflow]: <https://github.com/sphinx-contrib/zopeext/actions/workflows/tests.yaml>


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
