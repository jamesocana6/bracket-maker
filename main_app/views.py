from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class Tournament():
    def __init__(self, name, venue, players, prize_pool, is_complete = False):
        self.name = name
        self.venue = venue
        self.players = players
        self.prize_pool = prize_pool
        self.is_complete = is_complete

tournaments = [
    Tournament("The Big House 4", "University of Michigan", ["Mang0", "Plup", "Lucky", "Hungrybox", "Mew2King"], 20000),
    Tournament("Smash Summit 9", "Summit House", ["Mang0", "Plup", "Zain", "Hungrybox", "Amsa"], 40000, True),
    Tournament("RPS", "Zoom Call", ["James", "Kyler", "Peter", "Drew", "Sylvia"], 40000, True),
]
        

def tournaments_index(request):
    return render(request, "tournaments/index.html", {"tournaments" : tournaments})