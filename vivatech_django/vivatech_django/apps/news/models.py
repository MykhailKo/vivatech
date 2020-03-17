from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    preview_image = models.ImageField(upload_to='news', blank=True)
    text = models.TextField()
    images = ArrayField(models.ImageField(blank=True), blank=True)

    def recent(self):
        return self.pub_date >= (timezone.now() - timezone.timedelta(days=1))

    def __str__(self):
        return self.title
