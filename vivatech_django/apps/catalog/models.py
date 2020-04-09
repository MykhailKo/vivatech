from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, help_text = _('Name of your category'), verbose_name = _('name'))
    icon = models.ImageField(upload_to='icons_category', help_text="50px50px", verbose_name = _('icon'))#TBD

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class SubCategory(models.Model):
    name = models.CharField(max_length=200, help_text = _('Name of your sub category'), verbose_name = _('name'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = _('category'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Sub category")
        verbose_name_plural = _("Sub categories")


class Item(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name = _('sub category'))
    preview_image = models.ImageField(upload_to='items', blank=True, help_text="150px150px", verbose_name = _('preview image'))#TBD
    model = models.CharField(max_length=200, help_text = _('Name of your model'), verbose_name = _('Model name'))
    producer = models.CharField(max_length=200, blank=True, help_text = _('Producer name'), verbose_name = _('producer'))
    producer_logo = models.ImageField(upload_to='logos', blank=True, help_text="50px50px", verbose_name = _('producer logo'))#TBD
    country = models.CharField(max_length=200, help_text = _('Country of manufacture'), verbose_name = _('country'))
    pub_date = models.DateTimeField(verbose_name = _('date published'))
    description = models.TextField(verbose_name = _('description'))
    characteristics_ru = ArrayField(models.CharField(max_length=200, verbose_name = _('characteristics')), default=list)
    characteristics_uk = ArrayField(models.CharField(max_length=200, verbose_name=_('characteristics')), default=list)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")


class Review(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    autor = models.CharField(max_length=50, verbose_name = _('author name'))
    text = models.CharField(max_length=400, verbose_name = _('comment'))
    pub_date = models.DateTimeField(verbose_name = _('data published'))

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
