.ONESHELL:

.DEFAULT_GOAL := run

PYTHON := python
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: build run clean lint format test check

build: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run: build
	$(VENV_PYTHON) run.py

clean:
	rm -rf $(VENV) __pycache__ .pytest_cache

lint:
	$(VENV)/bin/pylint app tests

format:
	$(VENV)/bin/black app tests

test:
	-coverage run -m pytest tests -vv -s
	@echo "TEST COVERAGE REPORT"
	coverage report -m 

check: lint test