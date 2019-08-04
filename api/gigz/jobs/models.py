from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Job(models.Model):
    name = models.CharField(max_length = 30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.TextField()
    hours = models.FloatField()
    rate = models.FloatField()

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)