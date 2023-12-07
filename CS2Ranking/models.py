from django.db import models

# Create your models here.

class Player(models.Model):
    nickname = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40);
    age = models.IntegerField()
    nationality = models.CharField(max_length=40)
    current_team = models.CharField(max_length=40)

class Team(models.Model):
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    world_ranking = models.IntegerField()
    coach = models.CharField(max_length=40)
    rosters = models.ManyToManyField(Player)