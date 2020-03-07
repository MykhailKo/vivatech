from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news_main'),
    #path('<str:art_title>/', views.news_detail, name='news_detail')
]