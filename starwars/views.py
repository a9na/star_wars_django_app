from django.shortcuts import render, get_object_or_404
from .models import Character, Planet, Starship

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'starwars/character_list.html', {'characters': characters})

def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'starwars/character_detail.html', {'character': character})

def planet_list(request):
    planets = Planet.objects.all()
    return render(request, 'starwars/planet_list.html', {'planets': planets})

def starship_list(request):
    starships = Starship.objects.all()
    return render(request, 'starwars/starship_list.html', {'starships': starships})
