from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='icons_category', help_text="50px50px")#TBD

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    preview_image = models.ImageField(upload_to='items', blank=True, help_text="150px150px")#TBD
    model = models.CharField(max_length=200)
    producer = models.CharField(max_length=200, blank=True)
    producer_logo = models.ImageField(upload_to='logos', blank=True, help_text="50px50px")#TBD
    country = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.TextField()
    characteristics = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.model


class Review(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    autor = models.CharField('author name', max_length=50)
    text = models.CharField('comment', max_length=400)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.autor
