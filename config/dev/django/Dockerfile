FROM python:3.6
LABEL maintainer="info@rubyfire.ru"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

RUN pip install pipenv

COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
RUN pipenv install

COPY ../.. /code/
WORKDIR /code/

RUN pipenv run python manage.py migrate

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD exec pipenv run python manage.py runserver
