PYTHONPATH=./src/
PYTHON=./venv/bin/python

venv/bin/activate: requirements-dev.txt requirements.txt
	python -m venv venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -r requirements-dev.txt

install: venv/bin/activate

lint: venv/bin/activate
	@$(PYTHON) -m ruff check src/

format: venv/bin/activate
	@$(PYTHON) -m ruff format src/ $(ARGS)

test: venv/bin/activate
	PYTHONPATH=./src/ $(PYTHON) -m pytest --cov=src/ --cov-report=term --cov-report=html .

shell: venv/bin/activate
	@PYTHONPATH=./src/ $(PYTHON)

scratchpad: venv/bin/activate
	@PYTHONPATH=./src/ $(PYTHON) scratchpad.py

build: venv/bin/activate
	$(PYTHON) -m flit build

publish: venv/bin/activate
	$(PYTHON) -m flit publish

clean:
	rm -rf __pycache__
	rm -rf venv

.PHONY: clean install
