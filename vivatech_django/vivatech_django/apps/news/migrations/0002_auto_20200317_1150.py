# Generated by Django 3.0.3 on 2020-03-17 09:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, upload_to=''), blank=True, size=None),
        ),
    ]