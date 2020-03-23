# Generated by Django 3.0.4 on 2020-03-23 20:51

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Sub category', 'verbose_name_plural': 'Sub categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(help_text='50px50px', upload_to='icons_category', verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Name of your category', max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='characteristics',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='characteristics'), size=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='country',
            field=models.CharField(help_text='Country of manufacture', max_length=200, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='model',
            field=models.CharField(help_text='Name of your model', max_length=200, verbose_name='Model name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='preview_image',
            field=models.ImageField(blank=True, help_text='150px150px', upload_to='items', verbose_name='preview image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='producer',
            field=models.CharField(blank=True, help_text='Producer name', max_length=200, verbose_name='producer'),
        ),
        migrations.AlterField(
            model_name='item',
            name='producer_logo',
            field=models.ImageField(blank=True, help_text='50px50px', upload_to='logos', verbose_name='producer logo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.SubCategory', verbose_name='sub category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(help_text='Name of your sub category', max_length=200, verbose_name='name'),
        ),
    ]