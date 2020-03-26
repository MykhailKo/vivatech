from django.urls import path
from . import views


app_name = 'slider'

urlpatterns = [
    path('', views.home_slides_news, name='home'),
    path('sending_mail/', views.sending_mail, name='sending_mail'),
]
