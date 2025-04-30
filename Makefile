# Makefile for AI Voice Agent 🧠📞

APP_NAME=voice-agent
GCP_PROJECT_ID=your-gcp-project-id
REGION=us-central1
IMAGE=gcr.io/$(GCP_PROJECT_ID)/$(APP_NAME)
CLOUD_RUN_URL=https://$(APP_NAME)-$(REGION).a.run.app
PORT=8080

# 🐍 Python virtualenv
.PHONY: venv
venv:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# 🧪 Run Flask locally for dev
.PHONY: run
run:
	export FLASK_APP=app.py && flask run --port=$(PORT)

# 🧪 Run with Gunicorn (like prod)
.PHONY: serve
serve:
	gunicorn -b 0.0.0.0:$(PORT) app:app --reload

# 🧪 Test agent logic (can be expanded with pytest)
.PHONY: test
test:
	python -m unittest discover -s tests

# 🐳 Build Docker image
.PHONY: docker-build
docker-build:
	docker build -t $(APP_NAME) .

# 🐳 Run Docker locally
.PHONY: docker-run
docker-run:
	docker run -p $(PORT):$(PORT) $(APP_NAME)

# ☁️ Build + push to GCP Container Registry
.PHONY: gcloud-build
gcloud-build:
	gcloud builds submit --tag $(IMAGE)

# ☁️ Deploy to Google Cloud Run
.PHONY: gcloud-deploy
gcloud-deploy:
	gcloud run deploy $(APP_NAME) \
		--image $(IMAGE) \
		--platform managed \
		--region $(REGION) \
		--allow-unauthenticated

# 🔍 Check deployed URL
.PHONY: url
url:
	@echo "🚀 Deployed to: $(CLOUD_RUN_URL)"

# 🧹 Clean Docker images
.PHONY: clean
clean:
	docker rmi $(APP_NAME) || true
