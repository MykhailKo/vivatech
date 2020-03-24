from django.shortcuts import render
from django.http import HttpResponse
from .models import Slide
from .models import Slider
from news.models import News


def home_slides_news(request):
    slides = Slider.objects.all()
    news = News.objects.all().order_by('-pub_date')[0:3]
    return render(request, 'home/slides_news.html', {'slides': slides, 'news': news})