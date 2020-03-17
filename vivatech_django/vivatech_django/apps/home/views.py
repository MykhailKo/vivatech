from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide
from .models import Slider


#def home_slider(request):
#    slides = Slide.objects.all()
#    return render(request, 'home.html', {'slides' : slides})


def home_slider(request):
    slides = Slider.objects.all()
    return render(request, 'slide/slide.html', {'slides' : slides})

