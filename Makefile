PYTHON = python3.10
shell: .venv
	bash --init-file .init-file.bash

.venv:
	$(PYTHON) -m venv --clear $@
	.venv/bin/$(PYTHON) -m pip install --upgrade pip
	.venv/bin/$(PYTHON) -m pip install --upgrade pip .[test,doc]

test:
	nox

doc-server: .venv
	#poetry run sphinx-autobuild --re-ignore '_build|_generated' doc doc/_build/html
	. .venv/bin/activate && sphinx-autobuild --re-ignore '_build|_generated' doc doc/_build/html

clean:
	-rm -r .coverage
	-rm -r htmlcov
	-rm -r sphinxcontrib_zopeext.egg-info
	-rm -r dist
	-rm -r build
	-find . -name "__pycache__" -exec $(RM) -r {} +

.PHONY: shell test clean doc-server
