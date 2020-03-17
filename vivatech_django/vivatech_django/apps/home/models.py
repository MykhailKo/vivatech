from django.db import models


class Slide(models.Model):
    bg_image = models.ImageField()#TBD
    title = models.CharField(max_length=200)


class Slider(models.Model):
    bg_image = models.ImageField(upload_to='slider', blank=True)
    title = models.CharField(max_length = 80)
    text = models.TextField()
    btn_link = models.URLField(default='#')
    slide_order_number = models.IntegerField()

    def __str__(self):
        return self.title
