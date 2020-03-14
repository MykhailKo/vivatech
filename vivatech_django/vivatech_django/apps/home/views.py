from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide


def home_slider(request):
    slides = Slide.objects.all()
    return render(request, 'home/home.html', {'slides' : slides})
