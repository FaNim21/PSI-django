from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),

    path('<str:username>/ulubieni/add/<str:team_name>/', views.AddFavouriteTeamUser.as_view(), name='add_favourite_team_for_user'),
    path('<str:username>/ulubieni/get/', views.GetFavouriteTeamUser.as_view(), name='get_favourite_team_for_user'),
    path('<str:username>/ulubieni/remove/<str:team_name>/', views.RemoveFavouriteTeamUser.as_view(), name='remove_favourite_team_for_user'),

    path('<str:username>/match/<int:id>/comment/add/<str:text>', views.UserAddComment.as_view(), name='Add_comment'),
    path('<str:username>/comments/get', views.UserGetComments.as_view(), name='get_user_comments'),
    path('match/<int:id>/comments/get', views.MatchGetComments.as_view(), name='get_match_comments'),
]