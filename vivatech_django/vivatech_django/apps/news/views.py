from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import News, Category
from math import ceil


def news_main(request, page):
    page_size = 6
    start = page_size*(page-1)
    news = News.objects.all().order_by('-pub_date')[start:start+page_size]
    pages_num = range(1, ceil(news.count()/page_size) + 2)
    categories = Category.objects.all()
    return render(request, 'news/news_main.html', {'categories': categories, 'news': news, 'pages_num': pages_num, 'cur_page': page})


def news_detail(request, category, page, art_title):
    article = get_object_or_404(News, title = art_title)
    latest_news = News.objects.all().order_by('-pub_date')[:2]
    return render(request, 'news/news_detail.html', {'article': article, 'latest_news': latest_news, 'cur_page': page})


def news_order_by_category(request, category, page):
    page_size = 6
    start = page_size * (page - 1)
    news = News.objects.filter(category__name=category).order_by('-pub_date')[start:start + page_size]
    pages_num = range(1, ceil(news.count() / page_size) + 2)
    categories = Category.objects.all()
    return render(request, 'news/news_main.html', {'cur_category': category, 'categories': categories, 'news': news, 'pages_num': pages_num, 'cur_page': page})

