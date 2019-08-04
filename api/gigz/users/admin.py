from django.contrib import admin
from users.models import GigzEmployerUserProfile, GigzUserProfile, GigzWorkerUserProfile

# Register your models here.

admin.site.register(GigzUserProfile)
admin.site.register(GigzEmployerUserProfile)
admin.site.register(GigzWorkerUserProfile)
