# Generated by Django 3.0.4 on 2020-04-01 09:30

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
                ('name', models.CharField(help_text='Name of your category', max_length=200, verbose_name='name')),
                ('name_ru', models.CharField(help_text='Name of your category', max_length=200, null=True, verbose_name='name')),
                ('name_uk', models.CharField(help_text='Name of your category', max_length=200, null=True, verbose_name='name')),
                ('icon', models.ImageField(help_text='50px50px', upload_to='icons_category', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview_image', models.ImageField(blank=True, help_text='150px150px', upload_to='items', verbose_name='preview image')),
                ('model', models.CharField(help_text='Name of your model', max_length=200, verbose_name='Model name')),
                ('model_ru', models.CharField(help_text='Name of your model', max_length=200, null=True, verbose_name='Model name')),
                ('model_uk', models.CharField(help_text='Name of your model', max_length=200, null=True, verbose_name='Model name')),
                ('producer', models.CharField(blank=True, help_text='Producer name', max_length=200, verbose_name='producer')),
                ('producer_ru', models.CharField(blank=True, help_text='Producer name', max_length=200, null=True, verbose_name='producer')),
                ('producer_uk', models.CharField(blank=True, help_text='Producer name', max_length=200, null=True, verbose_name='producer')),
                ('producer_logo', models.ImageField(blank=True, help_text='50px50px', upload_to='logos', verbose_name='producer logo')),
                ('country', models.CharField(help_text='Country of manufacture', max_length=200, verbose_name='country')),
                ('country_ru', models.CharField(help_text='Country of manufacture', max_length=200, null=True, verbose_name='country')),
                ('country_uk', models.CharField(help_text='Country of manufacture', max_length=200, null=True, verbose_name='country')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('description', models.TextField(verbose_name='description')),
                ('description_ru', models.TextField(null=True, verbose_name='description')),
                ('description_uk', models.TextField(null=True, verbose_name='description')),
                ('characteristics', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='characteristics'), size=None)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of your sub category', max_length=200, verbose_name='name')),
                ('name_ru', models.CharField(help_text='Name of your sub category', max_length=200, null=True, verbose_name='name')),
                ('name_uk', models.CharField(help_text='Name of your sub category', max_length=200, null=True, verbose_name='name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Sub category',
                'verbose_name_plural': 'Sub categories',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50, verbose_name='author name')),
                ('text', models.CharField(max_length=400, verbose_name='comment')),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Item')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.SubCategory', verbose_name='sub category'),
        ),
    ]
