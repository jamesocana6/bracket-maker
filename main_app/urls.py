from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tournament/", views.tournaments_home, name="tournaments_home"),
    path("about/", views.about, name="about"),
    path("user/<int:user_id>/", views.user_tournaments_index, name="user_tournaments_index"),
    path("user/<int:user_id>/create/", views.TournamentCreate.as_view(), name="user_tournaments_create"),
    path("tournament/<int:tournament_id>", views.tournaments_detail, name="tournaments_detail"),
]