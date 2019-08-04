from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from users.models import GigzUserProfile, GigzWorkerUserProfile, GigzEmployerUserProfile

from users.views import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GigzUserProfile
        exclude = ()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = GigzUserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GigzEmployerUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GigzEmployerUserProfile
        exclude = ()

class GigzEmployerUserProfileViewSet(viewsets.ModelViewSet):
    queryset = GigzEmployerUserProfile.objects.all()
    serializer_class = GigzEmployerUserProfileSerializer

class GigzWorkerUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GigzWorkerUserProfile
        exclude = ()

class GigzWorkerUserProfileViewSet(viewsets.ModelViewSet):
    queryset = GigzWorkerUserProfile.objects.all()
    serializer_class = GigzWorkerUserProfileSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'workers', GigzWorkerUserProfileViewSet)
router.register(r'employers',GigzEmployerUserProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]