from django.contrib import admin
from .models import Item, SubCategory, Category, Review
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class CatalogAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(Item, CatalogAdmin)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Review)
