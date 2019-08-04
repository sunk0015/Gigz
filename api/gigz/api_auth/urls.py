from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from api_auth.views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    url(r'^facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^twitter/$', twitter_success, name='twitter_login'),
]
