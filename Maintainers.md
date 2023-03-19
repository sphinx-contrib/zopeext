# Maintainer documentation

[![Test badge][]][GitHub Tests Workflow]

[Test badge]: <https://github.com/sphinx-contrib/zopeext/actions/workflows/tests.yaml/badge.svg>
[GitHub Tests Workflow]: <https://github.com/sphinx-contrib/zopeext/actions/workflows/tests.yaml>

This document contains notes for developers and packagers. End users probably want to
read `README`. 

## TL;DR

```bash
# Use your system to install python3.7 through python3.11 and pipx
pipx install nox
pipx install pdm

# Run all tests
nox

# Make documentation
make doc-server

# Open a shell for development
make shell
PYTHON=python3.10 make shell
```

## Testing

Testing requires [nox][], which can be installed as an external tool with [pipx][]:

```bash
pipx install nox
```

The complete test suite can then be run with:

```bash
nox
```

Note: this will test against all supported versions of python: you need to make sure
that these are available for [nox][] to use.

## PyPi Release

1.  Make sure the repository is up-to date.
2.  Ensure the version is incremented:
    -   `sphinxcontrib/zopeext/__init__.py` must be updated
    -   `pyproject.toml` must be updated
    -   `CHANGES` must contain a summary of the changes
3.  Make sure all changes are committed, including the version number
    changes.
4.  Tag the sources with [\`hg tag X.Y]{.title-ref}.
5.  Don\'t forget to `hg push -r main -r X.Y`. (You need to explicitly
    push the tag or else the corresponding git tag will not get pushed.)
6.  Temporarily modify the `setup.cfg` file to comment out the variables
    `tag_build = dev` and `tag_date = true` (do **not** commit this
    changes).
7.  Run [pdm build]{.title-ref}.
8.  Run [pdm publish]{.title-ref}.

(The following are old need updates.

7.  Run [poetry build]{.title-ref}.

8.  Run [poetry publish]{.title-ref}.

    You may need to first establish your credentials. See
    <https://python-poetry.org/docs/repositories/#configuring-credentials>

9.  Register and upload the new release
    `twine upload dist/sphinxcontrib-zopeext-*.tar.gz`.

10. Generate the documentation with `make -C doc zip`. (Note: you can
    install the required tools with `pip install .[docs]`. This build
    uses latexmk so I needed to disable my global `.latekmkrc`
    configuration which specified a different output directory and
    confused sphinx.)

11. \<Outdated: need to use <https://readthedocs.org>\> Upload the new
    documentation (`doc/_build/sphinxcontrib-zopeext-doc.zip`) to PyPi:
    <http://pypi.python.org/pypi?%3Aaction=pkg_edit&name=sphinxcontrib-zopeext>

## PDM

I tried using [Poetry][] to manage the dependencies, but it is very aggressive about
putting upper bounds on dependencies which led to [issue #9][].  After trying to wrestle
with this, and reading Henry Schreiner's article [Should You Use Upper Bound Version
Constraints?][] (No!), I have decided to switch to [PDM][] for maintenance.  This
requires [PDM][] to be installed.

Further reading:

* [Should You Use Upper Bound Version Constraints?][]: Henry Schreiner's post which
  quite eloquently describes the issue.
* [Request: developers should be able to turn off dependency upper-bound calculations -
  poetry#2731](https://github.com/python-poetry/poetry/issues/2731): Example of the
  types of attitudes prevalent among the [Poetry][] maintainers.
* [Controlling PDM: Reproducibility vs. Convenience. -
  pdm#1758](https://github.com/pdm-project/pdm/discussions/1758): My discussion about
  how to use [PDM][] for development.  Until these questions are resolved, I will not
  explicitly used [PDM][] in the tool-chain, but developers can use it.
   
Here is how I switched from [Poetry][] to [PDM][]:

```bash
pdm init
Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
0. /data/apps/conda_arm64/envs/work/bin/python (3.9)
1. /opt/local/bin/python3.11 (3.11)
2. /opt/local/bin/python3.10 (3.10)
3. /opt/local/bin/python3.9 (3.9)
4. /data/apps/conda_arm64/envs/work/bin/python3.9 (3.9)
5. /usr/bin/python3 (3.9)
6. /opt/local/bin/python3.8 (3.8)
7. /opt/local/bin/python3.7m (3.7)
8. /opt/local/bin/python3.7 (3.7)
9. /Volumes/Data/apps/pipx/venvs/pdm/bin/python (3.9)
Please select (0): .2   
Using Python interpreter: /opt/local/bin/python3.10 (3.10)
Would you like to create a virtualenv with /opt/local/bin/python3.10? [y/n] (y): y
Virtualenv is created successfully at /Users/mforbes/current/zopeext_pdm/.venv
Is the project a library that will be uploaded to PyPI [y/n] (n): y
Project name (zopeext_pdm): sphinxcontrib-zopeext
Project version (0.1.0): 0.3.3
Project description (): Provides sphinxcontrib.zopeext.autointerface for documenting Zope interfaces.
Which build backend to use?
0. pdm-pep517
1. setuptools
2. flit
3. hatchling
4. pdm-backend
Please select (0): 4
License(SPDX name) (MIT): BSD-2-Clause
Author name (Michael McNeil Forbes): 
Author email (michael.forbes+numpy@gmail.com): mforbes@alum.mit.edu
Python requires('*' to allow any) (>=3.10): >=3.6.2
Changes are written to pyproject.toml.
```

After this, I needed to change the readme file from `README.MAINTAINER` (picked up by
mistake) to `README.rst`.   I have further changed the former to `Maintainers.md` as
GitHub was also picking up the wrong file.

```bash
pdm add zope.interface Sphinx
pdm add -G test sphinx[test] sphinx-testing pytest-cov importlib-metadata
pdm add -G doc sphinx-autobuild sphinx-book-theme
```

Our current version of `noxfile.py` was pretty heavily integrated with [Poetry][], using
it to determine the matrix of packages to test. I would like to fix this for use with
[PDM][] but am not sure how.  See:

* <https://github.com/pdm-project/pdm/issues/259#issuecomment-1407595572>

For now, I manually code the versions tested in `noxfile.py` (and in the CI files).

Some potentially helpful tools:

```python
core = pdm.core.Project(core, '.')
provider = core.get_provider()
provider._find_candidates(core.get_dependencies()['sphinx'])
```

[nox]: <https://nox.thea.codes/en/stable/config.html>
[pdm]: <https://pdm.fming.dev/latest/>
[poetry]: <https://python-poetry.org/>
[nox-poetry]: <https://github.com/cjolowicz/nox-poetry>
[issue #7]: <https://github.com/sphinx-contrib/zopeext/issues/7>
[issue #9]: <https://github.com/sphinx-contrib/zopeext/issues/9>
[Should You Use Upper Bound Version Constraints?]: 
  <https://iscinumpy.dev/post/bound-version-constraints/>

