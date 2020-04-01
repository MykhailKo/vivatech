# Generated by Django 3.0.4 on 2020-04-01 09:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_uk', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('country_ru', models.CharField(max_length=100, null=True, verbose_name='Country')),
                ('country_uk', models.CharField(max_length=100, null=True, verbose_name='Country')),
                ('brand_website', models.URLField(blank=True, default='#', verbose_name='Brand website')),
                ('logo', models.ImageField(upload_to='logos', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=300, verbose_name='Position')),
                ('position_ru', models.CharField(max_length=300, null=True, verbose_name='Position')),
                ('position_uk', models.CharField(max_length=300, null=True, verbose_name='Position')),
                ('requirements', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500, verbose_name='Requirements'), size=None)),
                ('responsibilities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500, verbose_name='Responsibilities'), size=None)),
                ('conditions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500, verbose_name='Conditions'), size=None)),
                ('priority', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=400, null=True, verbose_name='Title')),
                ('title_uk', models.CharField(max_length=400, null=True, verbose_name='Title')),
                ('icon', models.CharField(max_length=150, verbose_name='Icon')),
                ('icon_ru', models.CharField(max_length=150, null=True, verbose_name='Icon')),
                ('icon_uk', models.CharField(max_length=150, null=True, verbose_name='Icon')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Text')),
                ('text_uk', models.TextField(null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
