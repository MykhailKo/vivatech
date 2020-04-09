from django.db import models
from django.utils.translation import gettext_lazy as _


class Slide(models.Model):
    bg_image = models.ImageField()#TBD
    title = models.CharField(max_length=200, verbose_name = _('title'))

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")


class Slider(models.Model):
    bg_image = models.ImageField(upload_to='slider', blank=True, verbose_name=_("Backeground image"))
    title = models.CharField(max_length = 80, verbose_name = _('title'))
    text = models.TextField(verbose_name = _("text"))
    btn_link = models.URLField(default='#', verbose_name = _('Link'))
    slide_order_number = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")
