from django.shortcuts import render
from django.http import HttpResponse


def jobs_list(request):
    return HttpResponse('Hello jobs! Jobs application view for about page.')
