from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tournament/", views.tournaments_home, name="tournaments_home"),
    path("about/", views.about, name="about"),
    path("user/<int:user_id>/", views.user_tournaments_index, name="user_tournaments_index"),
    path("player/<int:player_id>/", views.player_tournaments_index, name="player_tournaments_index"),
    path("user/<int:user_id>/create/", views.TournamentCreate.as_view(), name="user_tournaments_create"),
    path("tournament/<int:tournament_id>", views.tournaments_detail, name="tournaments_detail"),
    path("tournament/<int:pk>/update/", views.TournamentUpdate.as_view(), name="tournaments_update"),
    path("tournament/<int:pk>/delete/", views.TournamentDelete.as_view(), name="tournaments_delete"),
    path('tournament/<int:tournament_id>/join/<int:player_id>/', views.join, name='join'),
    path("accounts/signup/", views.signup, name="signup"),

]