from django.shortcuts import render
from django.http import HttpResponse


def home_slider(request):
    return HttpResponse('Hello home! Slider application')
