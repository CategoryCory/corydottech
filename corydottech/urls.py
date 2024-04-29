from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path('', include('pages.urls')),
    path('cdt-admin/', admin.site.urls),
    path('api/', api.urls),
    path('tinymce/', include('tinymce.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
