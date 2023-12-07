from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from bs4 import BeautifulSoup


from .custom_views.rankingPlayer import (
    get_players
)


@api_view(["GET"])
def get_players_data(request):
    return get_players(request._request)

@api_view(["GET"])
def kadra_wmii(request):
    url = 'http://wmii.uwm.edu.pl/kadra'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, features="html.parser")
    table = soup.find('table', class_='views-table cols-8').find('tbody')

    list = []

    for row in table:
        degree = row.find('td', class_='views-field views-field-degree').text.strip()
        name = row.find('td', class_='views-field views-field-title active').text.strip()
        phone = row.find('td', class_='views-field views-field-field-phone').text.strip()

        email_td = row.find('td', class_='views-field views-field-field-email')
        email_span = email_td.find('span')

        if email_span:
            email_a = email_span.find('a')
            email = email_a.text.strip() if email_a else None
        else:
            email = None

        list.append(name)

        # print(degree, name, phone, email_td)
    return Response(list)
