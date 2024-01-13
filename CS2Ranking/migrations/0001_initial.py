# Generated by Django 4.1.7 on 2024-01-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('teamAResult', models.IntegerField(null=True)),
                ('teamBResult', models.IntegerField(null=True)),
                ('whoPicked', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40)),
                ('fullname', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=40)),
                ('current_team', models.CharField(max_length=40)),
                ('rating', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('nationality', models.CharField(max_length=40)),
                ('world_ranking', models.IntegerField()),
                ('coach', models.CharField(max_length=40)),
                ('rosters', models.ManyToManyField(to='CS2Ranking.player')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.CharField(max_length=40, null=True)),
                ('teamA', models.CharField(max_length=40, null=True)),
                ('teamB', models.CharField(max_length=40, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('maps', models.ManyToManyField(to='CS2Ranking.mapresult')),
            ],
        ),
    ]
