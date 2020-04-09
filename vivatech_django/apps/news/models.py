from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name = _('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = _('news'))
    title = models.CharField(max_length=200, verbose_name = 'title')
    pub_date = models.DateTimeField(_('date published'))
    preview_image = models.ImageField(upload_to='news', blank=True, verbose_name=_('preview image'))
    text = models.TextField(verbose_name = _('text'))
    images = ArrayField(models.ImageField(blank=True, verbose_name='images'), blank=True)

    def recent(self):
        return self.pub_date >= (timezone.now() - timezone.timedelta(days=1))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
