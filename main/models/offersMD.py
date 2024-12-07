from django.db import models
from ckeditor.fields import RichTextField

class OffersHeader(models.Model):
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)

    class Meta:
        verbose_name = "offers header"

class Offer(models.Model):
    icon = models.ImageField(verbose_name='offer icon', upload_to='offers_icons/', null=True, blank=True)
    title_ru = RichTextField(verbose_name="offer title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="offer title en", null=True, blank=True)
    description_ru = RichTextField(verbose_name="offer description ru", null=True, blank=True)
    description_en = RichTextField(verbose_name="offer description en", null=True, blank=True)