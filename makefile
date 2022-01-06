main:
	python -m pytest || exit 100
	rm -rf  dist/*
	# sdist is source code(create dist/ and pkg.egg-info/)
	# wheel is built package without go through the “build” process(create build/)
	python3 setup.py sdist bdist_wheel
	twine upload  dist/*

install:
	pip install -e .
	#-e git+https://somerepo/bar.git#egg=bar
	#-e /path/to/pkg

dev:
	python3 -m pip install build



