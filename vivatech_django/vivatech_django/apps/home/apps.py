from django.apps import AppConfig
from django.utils.translation import gettext_lazy as gl


class HomeConfig(AppConfig):
    name = 'home'
    verbose_name = gl("Home")
