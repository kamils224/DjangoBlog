from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from api import urls
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('auth/', obtain_auth_token)
]

urlpatterns += [

]
