from django.shortcuts import redirect
from django.utils import timezone
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Player


@api_view(['GET'])
def get_players(request):
    print(request)
    player = {'name': 'elo', 'nationality': 'poland'}
    return Response(player)
