from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from .models import Slide
from .models import Slider
from news.models import News


def home_slides_news(request):
    slides = Slider.objects.all()
    news = News.objects.all().order_by('-pub_date')[0:3]
    return render(request, 'home/slides_news.html', {'slides': slides, 'news': news})


def sending_mail(request):
    email = request.POST['footer_email']
    mail.send_mail(" Vivatech | Запрос на помощь в выборе", "Спасибо за Ваш запрос, мы скоро с Вами свяжемся. Ваша почта:" + email, "site@vivatec.com.ua", [email])
    mail.send_mail(" Vivatech | Запрос на помощь в выборе",
                   "Поступил запрос на поддержку с почты:" + email, "site@vivatec.com.ua",
                   ['tuareg1812@gmail.com'])
    return HttpResponseRedirect(reverse('home:home'))


def contacts_page(request):
    return render(request, 'home/contacts.html')


def contacts_send_mail(request):
    values = {
        'name': request.POST['full_name'],
        'email': request.POST['email'],
        'subject': request.POST['subject'],
        'text': request.POST['text'],
    }
    html_message = render_to_string('mail/main_form_mail.html', {'credits': values})
    plain_text_message = strip_tags(html_message)
    from_email = "site@vivatec.com.ua"
    to_email = ["tuareg1812@gmail.com"]

    mail.send_mail("vivatech.com: " + values['subject'], plain_text_message, from_email, to_email, html_message=html_message)
    return HttpResponseRedirect(reverse('home:contacts_page'))
    #return render(request, 'mail/main_form_mail.html', {'credits': values})
