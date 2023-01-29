test:
	nox

doc-server:
	poetry run sphinx-autobuild --re-ignore '_build|_generated' doc doc/_build/html

clean:
	-rm -r .coverage
	-rm -r htmlcov
	-rm -r sphinxcontrib_zopeext.egg-info
	-rm -r dist
	-rm -r build
	-find . -name "__pycache__" -exec $(RM) -r {} +

.PHONY: test clean doc-server
