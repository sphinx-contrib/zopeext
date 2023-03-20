PYTHON = python3.11
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
	$(RM) -r .coverage
	$(RM) -r htmlcov
	$(RM) -r sphinxcontrib_zopeext.egg-info
	$(RM) -r dist
	$(RM) -r build
	-find . -name "__pycache__" -exec $(RM) -r {} +

realclean: clean
	$(RM) -r .venv/

.PHONY: shell test clean realclean doc-server
