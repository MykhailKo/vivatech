from django.contrib import admin
from .models import Job, Brand, Service
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class JobAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(Job, JobAdmin)
admin.site.register(Brand)
admin.site.register(Service)

# Register your models here.
