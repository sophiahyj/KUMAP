from django.shortcuts import render, redirect
from .models import Building, Entrance, Facility

# Create your views here.
def index(request):
    entrances = Entrance.objects.all()
    photo = Entrance.objects.all()
    return render(request, 'index.html', {'entrances': entrances})