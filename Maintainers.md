# Maintainer documentation

[![Test badge][]][GitHub Tests Workflow]
[![PyPI badge][]][PyPI link]
[![gh: tag badge][]][gh: tags]
[![Coverage badge][]][Coverage link]
[![Documentation status badge][]][Documentation link]
[![Python versions badge][]][PyPI link]

[![open-ssf badge][]][open-ssf link]

[![gh: tag badge][]][gh: tags]
[![gh: forks badge][]][gh: forks]
[![gh: contributors badge][]][gh: contributors]
[![gh: stars badge][]][gh: stars]
[![gh: issues badge][]][gh: issues]


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


This document contains notes for developers and packagers. End users probably want to
read [`README.md`](README.md). 


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
2.  (Optional) Make a PR on GitHub.  I do it in the following steps (using [Hg-Git][]):

    ```bash
    hg topic X.Y
    hg bookmark X.Y
    hg push -r X.Y
    ```
    
    This prompts to create a PR at
    `https://github.com/sphinx-contrib/zopeext/pull/new/X.Y`.  The PR will allow you to
    review the changes.
3.  Ensure the version is incremented:
    -   `src/sphinxcontrib/zopeext/__version__.py` must be updated.
    -   `CHANGES` must contain a summary of the changes
4.  Make sure all changes are committed, including the version number
    changes and review these.
5.  Trigger a build of the `X.Y` on [Read The Docs][].  (Until you merge this with the
    `main` branch, you may need to [make X.Y an active
    version](https://readthedocs.org/projects/zopeext/versions/).)  Check that this
    looks okay.
6.  Once everything looks good, temporarily modify the `setup.cfg` file to comment out
    the variables `tag_build = dev` and `tag_date = true` (do **not** commit this
    changes).
7.  Publish to [PyPI][]:

    ```bash
    pdm build
    pdm publish
    ```

    You may need to first establish your credentials https://pypi.org/manage/account/token/. See
    <https://pdm.fming.dev/latest/usage/project/#configure-the-repository-secrets-for-upload>

    Fix any issues as needed.
8.  Tag the sources with `hg tag -m X.Y`.
9.  Push the tag `hg push -r X.Y`, and merge into the main branch or complete the merge
    request. If pushing, you need to explicitly push the tag or else the corresponding
    git tag will not get pushed.
    
10. Revert `setup.cfg`, update `__version__.py` to the next version `X.Z.dev0`,
    create a new topic, and push:

    ```bash
    hg revert setup.cfg
    vi src/sphinxcontrib/zopeext/__version__.py
    hg topic X.Z
    hg bookmark X.Z
    hg com -m "BRN: Start working on X.Z"
    hg push -r X.Z
    ```

## CI

I am currently using [GitHub][]'s continuous integration (CI) tools.  These are set up in
the [`.github/workflows`](.github/workflows) folder and include:

* Testing: [![Test badge][]][GitHub Tests Workflow].
* Coverage: [![Coverage badge][]][Coverage link].  Currently done with [Coveralls][].
* [Security
  Analysis](https://github.com/sphinx-contrib/zopeext/settings/security_analysis).
  Currently done with [CodeQL][].

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

[GitHub]: <github.com>
[nox]: <https://nox.thea.codes/en/stable/config.html>
[pdm]: <https://pdm.fming.dev/latest/>
[poetry]: <https://python-poetry.org/>
[nox-poetry]: <https://github.com/cjolowicz/nox-poetry>
[issue #7]: <https://github.com/sphinx-contrib/zopeext/issues/7>
[issue #9]: <https://github.com/sphinx-contrib/zopeext/issues/9>
[Should You Use Upper Bound Version Constraints?]: 
  <https://iscinumpy.dev/post/bound-version-constraints/>
[hg-git]: <https://hg-git.github.io/>
[Read the Docs]: <https://readthedocs.org/projects/zopeext/>
[Coveralls]: <https://coveralls.io/>
[CodeQL]: <https://codeql.github.com/>
