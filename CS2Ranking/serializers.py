from rest_framework import serializers

from CS2Ranking.models import Player, Team, Match, MapResult


class PlayerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['nickname']


class TeamSerializer(serializers.ModelSerializer):
    rosters = PlayerNameSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['name', 'nationality', 'world_ranking', 'coach', 'rosters']


class TeamNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']


class PlayerSerializer(serializers.ModelSerializer):
    current_team = TeamNameSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['nickname', 'fullname', 'age', 'nationality', 'rating', 'current_team']


class MapResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapResult
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    maps = MapResultSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['tournament', 'teamA', 'teamB', 'time', 'maps', 'live_viewers']
