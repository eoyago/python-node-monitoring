FROM python:3.11-slim

WORKDIR /app

COPY app/ ./app

CMD ["python", "./app/monitor.py"]