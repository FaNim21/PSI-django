from django.db import models


# Create your models here.

class Player(models.Model):
    nickname = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40);
    age = models.IntegerField()
    nationality = models.CharField(max_length=40)
    current_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)
    rating = models.FloatField(null=True)


class Team(models.Model):
    name = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40)
    world_ranking = models.IntegerField()
    coach = models.CharField(max_length=40)
    rosters = models.ManyToManyField(Player)


class MapResult(models.Model):
    name = models.CharField(max_length=40, null=True)
    teamAResult = models.IntegerField(null=True)
    teamBResult = models.IntegerField(null=True)
    whoPicked = models.CharField(max_length=40, null=True)


class Match(models.Model):
    tournament = models.CharField(max_length=40, null=True)
    teamA = models.CharField(max_length=40, null=True)
    teamB = models.CharField(max_length=40, null=True)
    time = models.DateTimeField(null=True)
    maps = models.ManyToManyField(MapResult)
    live_viewers = models.IntegerField(null=True)
