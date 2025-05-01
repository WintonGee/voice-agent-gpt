# Makefile — Phase 3: Cloud Run Deployment ☁️🧠

# =========
# SETTINGS
# =========

VENV_NAME=venv
PYTHON=$(VENV_NAME)/bin/python
PROJECT_ID=your-google-cloud-project-id
SERVICE_NAME=voice-agent
REGION=us-central1

# ===============
# ENVIRONMENT VARS
# (Pulled from .env and passed to deploy)
# ===============

include .env

ENV_VARS=\
  SENDGRID_API_KEY=$(SENDGRID_API_KEY),\
  OPENAI_API_KEY=$(OPENAI_API_KEY),\
  ASSEMBLYAI_API_KEY=$(ASSEMBLYAI_API_KEY),\
  CARTESIA_API_KEY=$(CARTESIA_API_KEY)

# ============
# ENV SETUP
# ============

.PHONY: venv
venv:
	python3 -m venv $(VENV_NAME)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: activate
activate:
	@echo "Run 'source $(VENV_NAME)/bin/activate' to activate the virtualenv"

# ===============
# LOCAL TESTING
# ===============

.PHONY: run
run:
	FLASK_APP=app.py FLASK_ENV=development flask run --port=8080

.PHONY: test
test:
	$(PYTHON) test_local.py

.PHONY: test_email
test_email:
	$(PYTHON) test_email.py

.PHONY: test_stt
test_stt:
	$(PYTHON) test_stt.py

# ===========
# DEPLOYMENT
# ===========

.PHONY: build
build:
	gcloud builds submit --project $(PROJECT_ID)

.PHONY: deploy
deploy:
	gcloud run deploy $(SERVICE_NAME) \
	  --source . \
	  --platform managed \
	  --region $(REGION) \
	  --allow-unauthenticated \
	  --project $(PROJECT_ID) \
	  --set-env-vars $(ENV_VARS)

.PHONY: logs
logs:
	gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=$(SERVICE_NAME)" --limit 50 --project $(PROJECT_ID) --format="value(textPayload)"

.PHONY: open
open:
	gcloud run services describe $(SERVICE_NAME) \
	  --platform managed \
	  --region $(REGION) \
	  --project $(PROJECT_ID) \
	  --format="value(status.url)"

# ===========
# CLEANUP
# ===========
.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache *.pyc $(VENV_NAME)
