# Generated by Django 3.0.4 on 2020-03-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(blank=True, upload_to='slider')),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('btn_link', models.URLField(default='#')),
                ('slide_order_number', models.IntegerField()),
            ],
        ),
    ]
