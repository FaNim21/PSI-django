# Generated by Django 4.1.7 on 2024-01-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS2Ranking', '0004_alter_player_current_team'),
        ('user', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='rankinguser',
            name='favourite_teams',
            field=models.ManyToManyField(to='CS2Ranking.team'),
        ),
    ]
