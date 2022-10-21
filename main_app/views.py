from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def tournaments_index(request):
    return render(request, "tournaments/index.html")