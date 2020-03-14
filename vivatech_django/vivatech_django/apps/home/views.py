from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider


def home_slider(request):
    slides = Slider.objects.all()
    return render(request, 'slide/slide.html', {'slides' : slides})
