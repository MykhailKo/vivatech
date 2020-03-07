from django.shortcuts import render
from django.http import HttpResponse


def main_categories(request):
    return HttpResponse('Hello catalog! Catalog application, view for list of main categories.')


def sub_category_list(request):
    return HttpResponse('Hello catalog! Catalog application, view for sub_category items list.')


def item_detail(request):
    return HttpResponse('Hello catalog! Catalog application, view for item details')
