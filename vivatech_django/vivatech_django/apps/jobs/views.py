from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _


def jobs_list(request):
    return HttpResponse(_('Hello jobs! Jobs application view for about page.'))
