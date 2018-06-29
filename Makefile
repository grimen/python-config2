
NAME := "config2"
BRANCH := $(shell git for-each-ref --format='%(objectname) %(refname:short)' refs/heads | awk "/^$$(git rev-parse HEAD)/ {print \$$2}")
HASH := $(shell git rev-parse HEAD)
DATETIME := $(shell date | sed 's/ /./g')

all: test

.PHONY: clean
clean:
	CLEAR_PATTERNS='*.pyc __pycache__ build dist *.egg-info .tox'; \
	for PATTERN in $$CLEAR_PATTERNS; do \
		echo "rm -rf \$$(find $$PWD -name $$PATTERN)"; \
		rm -rf $$(find $$PWD -name $$PATTERN); \
	done

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: install-ci
install-ci:
	pip install -U setuptools setuptools-git tox tox-travis && \
	pip install -r requirements.txt

.PHONY: test
test:
	python ./$(NAME)/tests

.PHONY: test-tox
test-tox:
	tox

.PHONY: test-ci
test-ci: test-tox

.PHONY: testimport
testimport:
	pip uninstall -y $(NAME) && \
	pip install -U . && \
	python -c "import $(NAME); print('$(NAME)', $(NAME))" && \
	echo "OK"

.PHONY: build
build:
	rm -rf ./dist && \
	python -m pip install --user --upgrade setuptools wheel && \
	python setup.py sdist bdist_wheel

.PHONY: dist
dist: build
	python -m pip install --user --upgrade twine && \
	twine upload dist/*

.PHONY: dist-dev
dist-dev: build
	python -m pip install --user --upgrade twine && \
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
