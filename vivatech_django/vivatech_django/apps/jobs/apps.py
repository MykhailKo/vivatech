from django.apps import AppConfig
from django.utils.translation import gettext_lazy as gl


class JobsConfig(AppConfig):
    name = 'jobs'
    verbose_name = gl('Jobs')
