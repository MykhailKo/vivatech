from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import News, Category


def news_main(request):
    categories = Category.objects.all()
    news = News.objects.all()
    return render(request, 'news/news_main.html', {'categories' : categories, 'news' : news})


# def news_order_by_category(request, category):
#     news = News.objects.filter(category = category)
#     return render(request, 'news/news_ordered.html', {'news' : news})


def news_detail(request, art_title):
    article = get_object_or_404(News, title = art_title)
    return render(request, 'news/news_detail.html', {'article' : article})
