from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Games(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now_add=True)
    solveTime = models.IntegerField()
    hintsCount = models.IntegerField()

