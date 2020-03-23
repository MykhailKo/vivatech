from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as gl


class Category(models.Model):
    name = models.CharField(max_length=200, help_text = gl('Name of your category'), verbose_name = gl('name'))
    icon = models.ImageField(upload_to='icons_category', help_text="50px50px", verbose_name = gl('icon'))#TBD

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = gl("Category")
        verbose_name_plural = gl("Categories")


class SubCategory(models.Model):
    name = models.CharField(max_length=200, help_text = gl('Name of your sub category'), verbose_name = gl('name'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = gl('category'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = gl("Sub category")
        verbose_name_plural = gl("Sub categories")


class Item(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = gl('sub category'))
    preview_image = models.ImageField(upload_to='items', blank=True, help_text="150px150px", verbose_name = gl('preview image'))#TBD
    model = models.CharField(max_length=200, help_text = gl('Name of your model'), verbose_name = gl('Model name'))
    producer = models.CharField(max_length=200, blank=True, help_text = gl('Producer name'), verbose_name = gl('producer'))
    producer_logo = models.ImageField(upload_to='logos', blank=True, help_text="50px50px", verbose_name = gl('producer logo'))#TBD
    country = models.CharField(max_length=200, help_text = gl('Country of manufacture'), verbose_name = gl('country'))
    pub_date = models.DateTimeField(verbose_name = gl('date published'))
    description = models.TextField(verbose_name = gl('description'))
    characteristics = ArrayField(models.CharField(max_length=200, verbose_name = gl('characteristics')))

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = gl("Item")
        verbose_name_plural = gl("Items")


class Review(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50, verbose_name = gl('author name'))
    text = models.CharField(max_length=400, verbose_name = gl('comment'))
    pub_date = models.DateTimeField(verbose_name = gl('data published'))

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = gl("Review")
        verbose_name_plural = gl("Reviews")
