from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import mail
from django.urls import reverse
from .models import Slide
from .models import Slider
from news.models import News


def home_slides_news(request):
    slides = Slider.objects.all()
    news = News.objects.all().order_by('-pub_date')[0:3]
    return render(request, 'home/slides_news.html', {'slides': slides, 'news': news})


def sending_mail(request):
    email = request.POST['email']
    mail.send_mail("Hello from Django", "This is {} new email adress".format(email), "email@gmail.com", [email])
    return HttpResponseRedirect(reverse('slide/slide.html'))
