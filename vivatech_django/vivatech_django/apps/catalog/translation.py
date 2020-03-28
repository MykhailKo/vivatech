from modeltranslation.translator import register, TranslationOptions
from .models import Category, SubCategory, Item

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('model', 'producer', 'country', 'description')
