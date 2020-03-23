from django.apps import AppConfig
from django.utils.translation import gettext_lazy as gl


class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = gl("Catalog")
