from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
from jobs.models import Job
from jobs.views import base
# Serializers define the API representation.
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        exclude = ()

# ViewSets define the view behavior.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

router = routers.DefaultRouter()
router.register(r'', JobViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', include(router.urls)),
    url(r'base', base),
]