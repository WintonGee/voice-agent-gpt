# Dockerfile — For Cloud Run
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PORT=8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
