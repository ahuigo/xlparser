main:
	python -m pytest -s
	rm -rf  dist/*
	# sdist is source code(dist/ and pkg.egg-info/)
	# wheel is built package without go through the “build” process(create build/)
	{ hash newversion.py 2>/dev/null && newversion.py version;} ;  { echo version `cat version`; }
	python3 setup.py sdist bdist_wheel
	twine upload  dist/*

	# one cli
	# python3 setup.py sdist bdist_wheel upload

install:
	pip install -e .
	#-e git+https://somerepo/bar.git#egg=bar
	#-e /path/to/pkg

test:
	pytest -s
