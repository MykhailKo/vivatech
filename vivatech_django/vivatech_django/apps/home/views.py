from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core import mail
from django.urls import reverse
from .models import Slide
from .models import Slider


def home_slider(request):
    slides = Slider.objects.all()
    return render(request, 'slide/slide.html', {'slides' : slides})


def sending_mail(request):
    email = request.POST['email']
    mail.send_mail("Hello from Django", "This is {} new email adress".format(email), "email@gmail.com", [email])
    return HttpResponseRedirect(reverse('slide/slide.html'))
