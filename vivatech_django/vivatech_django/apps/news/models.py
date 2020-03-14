from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=80)


    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    preview_image = models.ImageField(blank=True)
    text = models.TextField()
    images = ArrayField(models.ImageField(blank=True), blank=True)


    def __str__(self):
        return self.title
