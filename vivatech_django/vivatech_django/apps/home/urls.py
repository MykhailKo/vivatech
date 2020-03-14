from django.urls import path
from . import views

app_name = 'slider'

urlpatterns = [
    path('home/', views.home_slider, name='home'),
    path('', views.home_slider, name='home'),
]
