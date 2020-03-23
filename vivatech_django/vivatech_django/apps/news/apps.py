from django.apps import AppConfig
from django.utils.translation import gettext_lazy as gl


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = gl("News")
