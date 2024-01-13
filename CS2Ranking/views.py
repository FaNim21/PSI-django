from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

from rest_framework.views import APIView

from .models import Player, Team, Match
from .serializers import PlayerSerializer, TeamSerializer, MatchSerializer


# ======================================================
# PLAYERS
class PlayerView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        data = {'players': serializer.data}
        return JsonResponse(data, safe=False)


class PlayerIDView(APIView):
    def get(self, request, pk):
        player = Player.objects.get(id=pk)
        serializer = PlayerSerializer(player)
        data = {'player': serializer.data}
        return JsonResponse(data, safe=False)


class PlayerRankingView(APIView):
    def get(self, request):
        players = Player.objects.all().order_by('-rating')
        serializer = PlayerSerializer(players, many=True)
        data = {'players': serializer.data}
        return JsonResponse(data, safe=False)


# ======================================================
# TEAMS
class TeamView(APIView):
    def get(self, request):
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        data = {'teams': serializer.data}
        print(data)
        return JsonResponse(data, safe=False)


class TeamRankingView(APIView):
    def get(self, request):
        team = Team.objects.all().order_by('world_ranking')
        serializer = TeamSerializer(team, many=True)
        data = {'teams': serializer.data}
        return JsonResponse(data, safe=False)


# ======================================================
# MATCHES

class MatchView(APIView):
    def get(self, request):
        match = Match.objects.all()
        serializer = MatchSerializer(match, many=True)
        data = {'matches': serializer.data}
        return JsonResponse(data, safe=False)


class MatchTodayView(APIView):
    def get(self, request):
        today = datetime.date.today()
        matches_today = Match.objects.filter(time__date=today)
        serializer = MatchSerializer(matches_today, many=True)
        data = {'today_match': serializer.data}
        return JsonResponse(data, safe=False)


class MatchByDateView(APIView):
    def get(self, request, date):
        date_format = "%Y-%m-%d"
        result = datetime.datetime.strptime(date, date_format)
        matches = Match.objects.filter(time__date=result)
        serializer = MatchSerializer(matches, many=True)
        data = {f'matches {date}': serializer.data}
        return JsonResponse(data, safe=False)


class MatchPopularView(APIView):
    def get(self, request):
        matches_popular = Match.objects.filter(live_viewers__gt=30000)
        serializer = MatchSerializer(matches_popular, many=True)
        data = {'matches': serializer.data}
        return JsonResponse(data, safe=False)


# ======================================================
# GENERAL
class SearchTeamAndPlayerView(APIView):
    def get(self, request, name):
        result = name.strip()
        if not result:
            return JsonResponse({'data': 'empty'}, safe=False)

        players = Player.objects.filter(nickname__icontains=result)
        serializer_players = PlayerSerializer(players, many=True)
        teams = Team.objects.filter(name__icontains=result)
        serializer_teams = TeamSerializer(teams, many=True)
        data = {'players': serializer_players.data, 'teams': serializer_teams.data}
        return JsonResponse(data, safe=False)


class SearchAllView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer_players = PlayerSerializer(players, many=True)
        teams = Team.objects.all()
        serializer_teams = TeamSerializer(teams, many=True)
        data = {'players': serializer_players.data, 'teams': serializer_teams.data}
        return JsonResponse(data, safe=False)












