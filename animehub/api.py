from django.urls import path, include

from animehub.base import urls as base_urls
from animehub.catalog import urls as catalog_urls


urlpatterns = [
    path('pages/', include(base_urls)),
    path('catalog/', include(catalog_urls)),
]
