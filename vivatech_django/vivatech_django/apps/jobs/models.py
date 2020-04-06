from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class Job(models.Model):
    position = models.CharField(max_length=300, verbose_name=_("Position"))
    requirements_ru = ArrayField(models.CharField(max_length=500, verbose_name=_("Requirements")), default=list)
    requirements_uk = ArrayField(models.CharField(max_length=500, verbose_name=_("Requirements")), default=list)
    responsibilities_ru = ArrayField(models.CharField(max_length=500, verbose_name=_("Responsibilities")), default=list)
    responsibilities_uk = ArrayField(models.CharField(max_length=500, verbose_name=_("Responsibilities")), default=list)
    conditions_ru = ArrayField(models.CharField(max_length=500, verbose_name=_("Conditions")), default=list)
    conditions_uk = ArrayField(models.CharField(max_length=500, verbose_name=_("Conditions")), default=list)
    priority = models.IntegerField()

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    country = models.CharField(max_length=100, verbose_name=_("Country"))
    brand_website = models.URLField(default='#', blank=True, verbose_name=_("Brand website"))
    logo = models.ImageField(upload_to="logos", verbose_name=_("Logo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class Service(models.Model):
    title = models.CharField(max_length=400, verbose_name=_("Title"))
    icon = models.CharField(max_length=150, verbose_name=_("Icon"))
    text = models.TextField(verbose_name=_("Text"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
