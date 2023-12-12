"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CS2Ranking.views import PlayerView, PlayerIDView, PlayerRankingView
from CS2Ranking.views import TeamView, TeamRankingView
from CS2Ranking.views import MatchView, MatchTodayView
from CS2Ranking.views import SearchTeamAndPlayerView, SearchAllView

# docker build -t cs2ranking .
# docker run -dp 127.0.0.1:8000:8000 cs2ranking

urlpatterns = [
    path('admin/', admin.site.urls),

    path('players/', PlayerView.as_view(), name='players_list'),
    path('players/<int:pk>/', PlayerIDView.as_view(), name='player_list_id'),
    path('players/ranking/', PlayerRankingView.as_view(), name='players_list_ranking'),

    path('teams/', TeamView.as_view(), name='teams_list'),
    path('teams/ranking/', TeamRankingView.as_view(), name='teams_list_ranking'),

    path('matches/', MatchView.as_view(), name='matches_list'),
    path('matches/today/', MatchTodayView.as_view(), name='match_list_today'),

    path('search/<str:output>/', SearchTeamAndPlayerView.as_view(), name='search_team_and_player'),
    path('search/', SearchAllView.as_view(), name='search_team_and_player')
]
