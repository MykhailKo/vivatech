from modeltranslation.translator import register, TranslationOptions
from .models import Slide, Slider

@register(Slide)
class SlideTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
