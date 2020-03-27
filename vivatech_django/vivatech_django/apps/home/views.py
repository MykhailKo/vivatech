from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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


def contacts_page(request):
    return render(request, 'home/contacts.html')


def contacts_send_mail(request):
    name = request.POST['full_name']
    email = request.POST['email']
    subject = request.POST['subject']
    text = request.POST['text']
    #mail.send_mail("vivatech.com: " + subject, text, "vivatech@mail.com", ["vivatech@mail.com", "tuareg1812@gmail.com"])
    # return HttpResponse("<html><body>" + name + "<br>" + email + "<br>" + subject + "<br>" + text + "<br>" + "</body></html>")
    return HttpResponseRedirect(reverse('home:contacts_page'))
