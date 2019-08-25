from django.urls import path, include
from animehub.base import urls as base_urls


urlpatterns = [
    path('pages/', include(base_urls)),
]
