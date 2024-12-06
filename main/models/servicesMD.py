from django.db import models
from ckeditor.fields import RichTextField

class ServicesHeader(models.Model):
    title_uz = RichTextField(verbose_name="header title uz")
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)

    class Meta:
        verbose_name = "services header"

class Service(models.Model):
    title_uz = RichTextField(verbose_name="service title uz")
    title_ru = RichTextField(verbose_name="service title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="service title en", null=True, blank=True)
    description_uz = RichTextField(verbose_name="service description uz")
    description_ru = RichTextField(verbose_name="service description ru", null=True, blank=True)
    description_en = RichTextField(verbose_name="service description en", null=True, blank=True)

    class Meta:
        verbose_name = "service"