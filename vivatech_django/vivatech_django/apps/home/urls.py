from django.urls import path
from . import views


app_name = 'slider'

urlpatterns = [
    path('', views.home_slides_news, name='home'),
    path('contacts/', views.contacts_page, name='contacts_page'),
    path('sending_mail/', views.sending_mail, name='sending_mail'),
    path('contacts/sending_mail', views.contacts_send_mail, name='contacts_send_mail'),
]
