from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers

from DjangoBlogAPI import settings
from api import urls
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
