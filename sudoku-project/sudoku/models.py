from django.db import models
from django.contrib.auth.models import User


class Games(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = foreign key in this database, primary key in User database
    startTime = models.DateTimeField(auto_now_add=True) 
    #timestamp added automatically upon saving to database
    solveTime = models.IntegerField() #saved as number of seconds
    hintsCount = models.IntegerField()
    difficultyChoices = [
        ('E', 'easy'),
        ('M', 'medium'),
        ('H', 'hard')
    ]
    difficulty = models.CharField(max_length=2, choices=difficultyChoices, default='M')
    # if no difficulty provided default to medium

