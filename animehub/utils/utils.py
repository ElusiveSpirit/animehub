from django.apps import apps
from django.db.models import Model


def get_model(model_name: str) -> Model:
    """
    Return django model Class from app and name
    """
    return apps.get_model(*model_name.split('.'))


def get_model_app_name(obj: Model) -> str:
    """
    Return app.ModelName for django model instance
    """
    return f'{obj._meta.app_label}.{obj._meta.object_name}'
