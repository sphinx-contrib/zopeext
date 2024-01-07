import os
import nox


def _has_venv(session):
    return not isinstance(session.virtualenv, nox.virtualenv.PassthroughEnv)


python_versions = ["3.7", "3.8", "3.9", "3.10", "3.11"]
sphinx_versions = {_p: ["4.5.0", "5.3.0", "6.1.3", "7.2.6"] for _p in python_versions}

# These are in the full matrix, but excluded by the constraints in pyproject.toml.  Not
# sure how to exclude these programmatically yet with pdm.
# https://github.com/pdm-project/pdm/issues/259#issuecomment-1407595572
excluded_versions = {
    ("3.7", "6.1.3"),
}

python_sphinx = [
    (python, sphinx)
    for python in python_versions
    for sphinx in sphinx_versions[python]
    if (python, sphinx) not in excluded_versions
]


@nox.session(reuse_venv=True)
@nox.parametrize("python,sphinx", python_sphinx)
def test(session, sphinx):
    """Run the test suite."""

    # If a virtual environment is used, configure PDM appropriately and install
    # If --no-venv is used, the install step is skipped
    if _has_venv(session):
        # os.environ.update({"PDM_USE_VENV": "1", "PDM_IGNORE_SAVED_PYTHON": "1"})
        # session.run("pdm", "install", "-G", "tests", external=True)
        # session.run("pdm", "install", "--dev", external=True)
        # session.run("pdm", "run", "pip", "install", f"sphinx[test]=={sphinx}",
        # external=True)
        session.install(".[test]", f"sphinx[test]~={sphinx}")
    session.run("pytest", "tests")
