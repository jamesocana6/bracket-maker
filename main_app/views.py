from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Host, Tournament, Player
from datetime import date, datetime, timedelta

# class Tournament():
#     def __init__(self, name, venue, players, prize_pool, is_complete = False):
#         self.name = name
#         self.venue = venue
#         self.players = players
#         self.prize_pool = prize_pool
#         self.is_complete = is_complete

# tournaments = [
#     Tournament("The Big House 4", "University of Michigan", ["Mang0", "Plup", "Lucky", "Hungrybox", "Mew2King"], 20000),
#     Tournament("Smash Summit 9", "Summit House", ["Mang0", "Plup", "Zain", "Hungrybox", "Amsa"], 40000, True),
#     Tournament("RPS", "Zoom Call", ["James", "Kyler", "Peter", "Drew", "Sylvia"], 40000, True),
# ]

def home(request):
    return redirect("tournaments/")

def tournaments_home(request):
    tournaments = Tournament.objects.all()
    today = date.today()
    past = tournaments.filter(date__lt=today)
    upcoming = tournaments.filter(date__gte=today)
    return render(request, "home.html", {
        "tournaments" : tournaments,
        "past": past,
        "upcoming": upcoming,
    })

def tournaments_detail(request, tournament_id):
    tournament = Tournament.objects.get(id = tournament_id)
    joined = tournament.max_players - len(tournament.players.all())
    return render(request, "tournament/detail.html", {
        "range" : range(int(tournament.max_players/2)),
        "tournament" : tournament,
        "joined": joined,
        })

def about(request):
    return render(request, "about.html")

def user_tournaments_index(request, user_id):
    user = User.objects.get(id = user_id)
    tournaments = user.tournament_set.all()
    today = date.today()
    past = tournaments.filter(date__lt=today)
    upcoming = tournaments.filter(date__gte=today)
    return render(request, "user_tournaments/index.html", {
        "tournaments" : tournaments,
        "page_user": user,
        "past": past,
        "upcoming": upcoming,
    })

def player_tournaments_index(request, player_id):
    user = Player.objects.get(id = player_id)
    tournaments = user.tournament_set.all()
    today = date.today()
    past = tournaments.filter(date__lt=today)
    upcoming = tournaments.filter(date__gte=today)
    return render(request, "user_tournaments/index.html", {
        "tournaments" : tournaments,
        "page_user": user,
        "past": past,
        "upcoming": upcoming,
    })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # TARGERS THE HOST CHECKBOX VALUE
      if request.POST.get("host"):
        print("REQUEST POST HOST", request.POST["host"])
        print("host")
        user = form.save()
        user.save()
        host = Host.objects.create(user=user)
        host.save()
        login(request, user)
      else:
        print("player")
        user = form.save()
        user.save()
        player = Player.objects.create(user=user)
        player.save()
        login(request, user)
      return redirect('user_tournaments_index', user.id)
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def join(request, tournament_id, player_id):
  # Note that you can pass a toy's id instead of the whole object
   Tournament.objects.get(id=tournament_id).players.add(player_id)
   return redirect('tournaments_detail', tournament_id=tournament_id)

class TournamentCreate(CreateView):
    model = Tournament
    fields = ["event_name", "date", "game", "venue", "max_players", "prize_pool"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TournamentUpdate(UpdateView):
    model = Tournament
    fields = ["event_name", "date", "game", "venue", "max_players", "prize_pool"]

class TournamentDelete(DeleteView):
    model = Tournament

    def get_success_url(self):
        return reverse('user_tournaments_index', kwargs={'user_id': self.object.user_id})

