FROM python:3.6
LABEL maintainer="info@rubyfire.ru"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

RUN pip install pipenv

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock
RUN pipenv install --system --dev --deploy --skip-lock

WORKDIR /app

EXPOSE 8000
