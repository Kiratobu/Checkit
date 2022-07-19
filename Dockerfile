# syntax=docker/dockerfile:1
FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code
RUN apt-get update \
    && apt-get  install -y \
    mc \
    vim
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock /code/
RUN pipenv install
RUN cd /code && pipenv lock --requirements > requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT

