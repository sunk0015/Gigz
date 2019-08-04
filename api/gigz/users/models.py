from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GigzUserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_lat = models.FloatField()
    location_lng = models.FloatField()

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return repr(self.user)

    
class GigzWorkerUserProfile(GigzUserProfile):
    completed_jobs = models.IntegerField()
    worker_rating = models.FloatField()
    worker_description = models.TextField()

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return repr(self.user)
    
class GigzEmployerUserProfile(GigzUserProfile):
    posted_jobs = models.IntegerField()
    employer_rating = models.FloatField()
    employer_description = models.TextField()

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return repr(self.user)