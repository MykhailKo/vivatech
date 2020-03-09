from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='category/icon_category')#TBD

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    preview_image = models.ImageField(upload_to='category/item_preview', blank=True)#TBD
    model = models.CharField(max_length=200)
    producer = models.CharField(max_length=200, blank=True)
    producer_logo = models.ImageField(upload_to='category/producer_logo', blank=True)#TBD
    country = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    characteristics = ArrayField(models.CharField(max_length=200))
    reviews = ArrayField(models.TextField(), blank=True)

    def __str__(self):
        return self.model

    def leave_review(self, text):
        self.reviews.append(text)
