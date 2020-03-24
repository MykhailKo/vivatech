from django.urls import path
from . import views


app_name = 'slider'

urlpatterns = [
    path('', views.home_slides_news, name='home'),
]
