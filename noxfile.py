"""

For a discussion about the parameterized versions of Sphinx, see

https://github.com/cjolowicz/nox-poetry/discussions/289

"""
import sys

from nox_poetry import session
import nox

sys.path.append(".")
from noxutils import get_versions


@session(python=["3.6", "3.7", "3.8", "3.9"], reuse_venv=True)
@nox.parametrize("sphinx", get_versions("sphinx", "minor"))
def test(session, sphinx):
    # nox_poetry uses the info in poetry.lock but you need to specify the test
    # dependencies here:
    session.install("sphinx-testing", "pytest-cov", ".")
    # Override sphinx, but using get_versions() makes sure this is consistent
    session.run("pip", "install", f"sphinx=={sphinx}")
    session.run("pytest")


@session(venv_backend="conda", python=["3.6", "3.7", "3.8", "3.9"])
def _test_conda(session):
    # session.conda_env_update("environment.yml")
    # session.conda("env", "update", "--f", "environment.yml",
    #              conda="mamba", external=True)
    session.install(".[test]")
    session.run("pytest")
