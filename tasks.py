# -*- coding: utf-8 -*-
"""Invoke tasks.py

Details see manual: http://docs.pyinvoke.org/en/1.0/getting-started.html
"""
# ThirdParty Library
from invoke import task


@task
def install(ctx):
    """Установка зависимостей сервиса."""
    ctx.run('pipenv install')


@task
def yapf(ctx):
    """Запуск yapf."""
    ctx.run(
        'yapf -i --recursive  animehub/'
    )


@task
def flake8(ctx):
    """Запуск flake8."""
    ctx.run(
        'flake8 animehub/'
    )


@task
def isort(ctx):
    """Запуск isort."""
    ctx.run(
        'isort -rc --atomic animehub/'
    )


@task(pre=[isort, yapf, flake8])
def lint(ctx):
    """Запуск линтеров."""
    pass
