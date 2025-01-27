from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


from . import api

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^api/v1/', include(api)),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
