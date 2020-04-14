from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.urls import reverse
from .models import Slide
from .models import Slider
from news.models import News


def home_slides_news(request):
    lang_codes = [c for (c, name) in settings.LANGUAGES]
    parts = request.get_full_path().split('/')
   # try:
   #     if request.session[LANGUAGE_SESSION_KEY]: 
   #         request.session[LANGUAGE_SESSION_KEY] = request.session[LANGUAGE_SESSION_KEY] 
   # except:
   #     request.session[LANGUAGE_SESSION_KEY] = 'uk'
    if parts[1] == 'en':
        parts[1] = 'uk'
        return redirect('/'.join(parts))
   # elif parts[1] == 'ru' and request.session[LANGUAGE_SESSION_KEY] != 'uk':
   #     parts[1] = 'ru'
   #     return redirect('/'.join(parts))
    elif parts[1] not in lang_codes:
        parts[0] = '/' + 'uk'
        return redirect('/'.join(parts))
    slides = Slider.objects.all().order_by('slide_order_number')
    news = News.objects.all().order_by('-pub_date')[0:3]
    return render(request, 'home/slides_news.html', {'slides': slides, 'news': news})


def sending_mail(request):
    email = request.POST['footer_email']
    mail.send_mail(" Vivatech | Запрос на помощь в выборе", "Спасибо за Ваш запрос, мы скоро с Вами свяжемся. Ваша почта:" + email, "site@vivatec.com.ua", [email])
    mail.send_mail(" Vivatech | Запрос на помощь в выборе",
                   "Поступил запрос на поддержку с почты:" + email, "site@vivatec.com.ua",
                   ['tuareg1812@gmail.com', 'office@vivatec.com.ua'])
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
    to_email = ["tuareg1812@gmail.com", 'office@vivatec.com.ua']

    mail.send_mail("vivatech.com: " + values['subject'], plain_text_message, from_email, to_email, html_message=html_message)
    return HttpResponseRedirect(reverse('home:contacts_page'))
    #return render(request, 'mail/main_form_mail.html', {'credits': values})
