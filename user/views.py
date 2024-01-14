from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from CS2Ranking.models import Team, Match
from CS2Ranking.serializers import TeamSerializer
from user.models import RankingUser, Comment
from user.serializers import UserSerializer, AuthTokenSerializer, CommentUserSerializer, CommentMatchSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user


class AddFavouriteTeamUser(APIView):
    def post(self, request, username, team_name):
        user = get_object_or_404(RankingUser, username=username)
        team = get_object_or_404(Team, name=team_name)
        user.favourite_teams.add(team)
        return JsonResponse({'message': f'Team {team_name} added to favourites for user {username}.'})


class GetFavouriteTeamUser(APIView):
    def get(self, request, username):
        user = get_object_or_404(RankingUser, username=username)
        favourite_teams = user.favourite_teams.all()
        serializer = TeamSerializer(favourite_teams, many=True)
        data = {'teams': serializer.data}
        return JsonResponse(data, safe=False)


class RemoveFavouriteTeamUser(APIView):
    def post(self, request, username, team_name):
        user = get_object_or_404(RankingUser, username=username)
        team = get_object_or_404(Team, name=team_name)
        user.favourite_teams.remove(team)
        return JsonResponse({'message': f'Team {team_name} is removed from favourites for user {username}.'})


class UserAddComment(APIView):
    def post(self, request, username, id, text):
        user = get_object_or_404(RankingUser, username=username)
        match = get_object_or_404(Match, id=id)
        comment = Comment.objects.create(ranking_user=user, match=match, text=text)
        return JsonResponse({'message': f'User: {user.name} added comment to match id: {id} with text {text}'})


class UserGetComments(APIView):
    def get(self, request, username):
        user = get_object_or_404(RankingUser, username=username)
        user_comments = Comment.objects.filter(ranking_user=user)
        serializer = CommentUserSerializer(user_comments, many=True)
        data = {'comments': serializer.data}
        return JsonResponse(data, safe=False)


class MatchGetComments(APIView):
    def get(self, request, id):
        match = get_object_or_404(Match, id=id)
        user_comments = Comment.objects.filter(match=match)
        serializer = CommentMatchSerializer(user_comments, many=True)
        data = {'comments': serializer.data}
        return JsonResponse(data, safe=False)

