# Makefile — Phase 1: Local testing only 🧠💻
# AI Voice Agent with GPT-4, Cartesia TTS, SendGrid

# ========
# SETTINGS
# ========

VENV_NAME=venv
PYTHON=$(VENV_NAME)/bin/python

# ===========
# ENV SETUP
# ===========

.PHONY: venv
venv:
	python3 -m venv $(VENV_NAME)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: activate
activate:
	@echo "Run 'source $(VENV_NAME)/bin/activate' to activate the virtualenv"

# ===========
# RUN/TEST
# ===========

# Run the CLI testing script
.PHONY: test
test:
	$(PYTHON) test_local.py

# ===========
# LINTING (OPTIONAL)
# ===========

.PHONY: lint
lint:
	flake8 agent.py tts.py emailer.py config.py

# ===========
# CLEAN
# ===========

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache *.pyc $(VENV_NAME)
