from modeltranslation.translator import register, TranslationOptions
from .models import Job, Brand, Service

@register(Job)
class JobTranslationOptions(TranslationOptions):
    fields = ('position',)


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name', 'country')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'icon', 'text')
