from django.db import models

class Slider(models.Model):
    bg_image = models.ImageField(blank=True)
    title = models.CharField(max_length = 80)
    text = models.TextField()
    btn_link = models.URLField(default='#')
    slide_order_number = models.IntegerField()

    def __str__(self):
        return self.title
