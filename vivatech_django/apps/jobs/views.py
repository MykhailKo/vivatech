from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Job, Brand, Service


def about_page(request):
    jobs = Job.objects.all().order_by('priority')
    brands = Brand.objects.all()
    services = Service.objects.all()
    return render(request, 'about/about.html', {'brands': brands, 'jobs': jobs, 'services': services})
