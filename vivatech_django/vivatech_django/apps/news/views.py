from django.shortcuts import render
from django.http import  HttpResponse


def news_main(request):
    return HttpResponse('Hello news! News application, view for all news.')


def news_detail(request):
    return HttpResponse('Hello news! News application, view for detailed news.')