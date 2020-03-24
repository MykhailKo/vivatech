from django.db import models
from django.contrib.postgres.fields import ArrayField


class Job(models.Model):
    position = models.CharField(max_length=300)
    requirements = ArrayField(models.CharField(max_length=500))
    responsibilities = ArrayField(models.CharField(max_length=500))
    conditions = ArrayField(models.CharField(max_length=500))
    priority = models.IntegerField()

    def __str__(self):
        return self.position


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    brand_website = models.URLField(default='#', blank=True)
    logo = models.ImageField(upload_to="logos")

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=400)
    icon = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title

