# Generated by Django 3.0.5 on 2020-04-01 18:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('name_ru', models.CharField(max_length=80, null=True, verbose_name='name')),
                ('name_uk', models.CharField(max_length=80, null=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_uk', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('preview_image', models.ImageField(blank=True, upload_to='news', verbose_name='preview image')),
                ('text', models.TextField(verbose_name='text')),
                ('text_ru', models.TextField(null=True, verbose_name='text')),
                ('text_uk', models.TextField(null=True, verbose_name='text')),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(blank=True, upload_to='', verbose_name='images'), blank=True, size=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='news')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
