test:
	python setup.py test

clean:
	-rm -r .coverage
	-rm -r htmlcov
	-rm -r sphinxcontrib_zopeext.egg-info
	-rm -r dist
	-rm -r build

.PHONY: test clean
