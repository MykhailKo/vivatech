from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_main, name='news_main'),
    # path('<str:category>/', views.news_order_by_category(), name='ordered_by'),
    path('<str:art_title>/', views.news_detail, name='news_detail'),
]
