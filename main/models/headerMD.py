from django.db import models
from ckeditor.fields import RichTextField

class Header(models.Model):
    title_ru = RichTextField(verbose_name="title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="title en", null=True, blank=True)
    text1_ru = RichTextField(verbose_name="text1 ru", null=True, blank=True)
    text1_en = RichTextField(verbose_name="text1 en", null=True, blank=True)
    text2_ru = RichTextField(verbose_name="text2 ru", null=True, blank=True)
    text2_en = RichTextField(verbose_name="text2 en", null=True, blank=True)
    image = models.ImageField(upload_to='header_images/', verbose_name="header image", null=True, blank=True)

    class Meta:
        verbose_name = "Header"