from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Item, SubCategory, Category, Review


def main_categories(request):
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    return render(request, 'catalog/catalog.html', {'categories' : categories, 'sub_categories' : sub_categories})


def sub_category_list(request, sub_cat_name):
    items = Item.objects.filter(sub_category__name = sub_cat_name)
    return render(request, 'catalog/category.html', {'items' : items, 'sub_cat_name' : sub_cat_name})


def item_detail(request, sub_cat_name, item_model):
    item = get_object_or_404(Item, model=item_model)
    reviews = item.review_set.order_by('-pub_date')
    return render(request, 'catalog/item.html', {"item" : item, "reviews" : reviews, "sub_cat_name" : sub_cat_name})


def leave_review(request, sub_cat_name, item_model):
    item = get_object_or_404(Item, model = item_model)
    item.review_set.create(autor = request.POST['full_name'], text = request.POST['text'], pub_date = timezone.now(), item_id = item)
    return HttpResponseRedirect(reverse('catalog:item_detail', args = (item.sub_category.name, item.model)))
