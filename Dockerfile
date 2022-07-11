FROM python:3.9-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
COPY ./src /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt




