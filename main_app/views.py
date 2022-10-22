from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Tournament

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
    return render(request, "home.html", {"tournaments" : tournaments})

def tournaments_detail(request, tournament_id):
    tournament = Tournament.objects.get(id = tournament_id)
    return render(request, "tournament/detail.html", {"tournament" : tournament})

def about(request):
    return render(request, "about.html")

def user_tournaments_index(request, user_id):
    user = User.objects.get(id = user_id)
    tournaments = user.tournament_set.all()
    return render(request, "user_tournaments/index.html", {
        "tournaments" : tournaments,
        "user": user,
    })

class TournamentCreate(CreateView):
    model = Tournament
    fields = ["event_name", "date", "game", "venue", "prize_pool"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)