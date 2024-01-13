from django.db.models import Q
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

from .models import Player, Team, Match


# ======================================================
# PLAYERS
class PlayerView(View):
    def get(self, request):
        players = Player.objects.all().values()
        data = {'players': list(players)}
        return JsonResponse(data, safe=False)


class PlayerIDView(DetailView):
    def get(self, request, pk):
        player = Player.objects.get(id=pk)
        data = {'player': model_to_dict(player)}
        return JsonResponse(data, safe=False)


class PlayerRankingView(View):
    def get(self, request):
        players = Player.objects.all().values().order_by('-rating')
        data = {'players': list(players)}
        return JsonResponse(data, safe=False)



# ======================================================
# TEAMS
class TeamView(View):
    def get(self, request):
        team = Team.objects.all().values()
        data = {'teams': list(team)}
        return JsonResponse(data, safe=False)


class TeamRankingView(View):
    def get(self, request):
        team = Team.objects.all().values().order_by('world_ranking')
        data = {'teams': list(team)}
        return JsonResponse(data, safe=False)



# ======================================================
# MATCHES

class MatchView(View):
    def get(self, request):
        match = Match.objects.all().values()
        data = {'matches': list(match)}
        return JsonResponse(data, safe=False)


class MatchTodayView(View):
    def get(self, request):
        today = datetime.date.today()
        matches_today = Match.objects.filter(time__date=today).values()
        data = {'today_match': list(matches_today)}
        return JsonResponse(data, safe=False)


class MatchByDateView(DetailView):
    def get(self, request, output):
        date_format = "%Y-%m-%d"
        result = datetime.datetime.strptime(output, date_format)

        matches = Match.objects.filter(time__date=result).values()
        data = {f'matches {output}': list(matches)}
        return JsonResponse(data, safe=False)



# ======================================================
# GENERAL
class SearchTeamAndPlayerView(DetailView):
    def get(self, request, output):
        result = output.strip()
        if not result:
            return JsonResponse({'data': 'empty'}, safe=False)

        players = Player.objects.filter(nickname__icontains=result).values()
        teams = Team.objects.filter(name__icontains=result).values()
        data = {'players': list(players), 'teams': list(teams)}
        return JsonResponse(data, safe=False)


class SearchAllView(View):
    def get(self, request):
        players = Player.objects.all().values()
        teams = Team.objects.all().values()
        data = {'players': list(players), 'teams': list(teams)}
        return JsonResponse(data, safe=False)












