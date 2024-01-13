from django.urls import path
from CS2Ranking.views import PlayerView, PlayerIDView, PlayerRankingView
from CS2Ranking.views import TeamView, TeamRankingView
from CS2Ranking.views import MatchView, MatchTodayView, MatchByDateView
from CS2Ranking.views import SearchTeamAndPlayerView, SearchAllView

# docker build -t cs2ranking .
# docker run -dp 127.0.0.1:8000:8000 cs2ranking

urlpatterns = [
    path('players/', PlayerView.as_view(), name='players_list'),
    path('players/<int:pk>/', PlayerIDView.as_view(), name='player_list_id'),
    path('players/ranking/', PlayerRankingView.as_view(), name='players_list_ranking'),

    path('teams/', TeamView.as_view(), name='teams_list'),
    path('teams/ranking/', TeamRankingView.as_view(), name='teams_list_ranking'),

    path('matches/', MatchView.as_view(), name='matches_list'),
    path('matches/today/', MatchTodayView.as_view(), name='match_list_today'),
    path('matches/<str:output>/', MatchByDateView.as_view(), name='match_list_today'),

    path('search/<str:output>/', SearchTeamAndPlayerView.as_view(), name='search_team_and_player'),
    path('search/', SearchAllView.as_view(), name='search_team_and_player')
]