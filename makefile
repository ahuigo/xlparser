msg?=
.ONESHELL:
gitcheck:
	if [[ "$(msg)" = "" ]] ; then echo "Usage: make pkg msg='commit msg'";exit 20; fi

install:
	pip install -e .
	#-e git+https://somerepo/bar.git#egg=bar
	#-e /path/to/pkg
install-git:
	pipx install git+https://github.com/ahuigo/xlparser.git

test:
	python3 -m pytest -s

###################### publish package #####################################
# poetry: make pkg msg='xx'
pkg: gitcheck test
	rm -rf  dist/*
	{ hash newversion.py 2>/dev/null && newversion.py pyproject.toml;} 	# one cli
	poetry build && poetry publish
	git commit -am "$(msg)"
	git push origin HEAD

############### how to create a new project with poetry? ##########################
# 1. create project package
create:
	poetry new mypkg

# 2. 生成poetry.lock + requirements.txt
lock:
	poetry lock
	poetry export --output requirements.txt
