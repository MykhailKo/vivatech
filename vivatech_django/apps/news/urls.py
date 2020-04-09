from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('<int:page>', views.news_main, name='news_main'),
    path('<str:category>/<int:page>', views.news_order_by_category, name='ordered_by'),
    path('<str:category>/<int:page>/<str:art_title>/', views.news_detail, name='news_detail'),
]
