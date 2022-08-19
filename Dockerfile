# syntax=docker/dockerfile:1
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system 
COPY . /code/
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT