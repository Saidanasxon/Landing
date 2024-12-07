from django.db import models
from ckeditor.fields import RichTextField

class Footer(models.Model):
    description_ru = RichTextField(verbose_name='Footer matni ru', null=True, blank=True)
    description_en = RichTextField(verbose_name='Footer matni en', null=True, blank=True)
    copyright_text_ru = RichTextField(verbose_name='Copyrigth text ru', null=True, blank=True)
    copyright_text_en = RichTextField(verbose_name='Copyrigth text en', null=True, blank=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footerlar"

    def __str__(self):
        return self.copyright_text_uz

class OurSocialMedia(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ijtimoiy tarmoq nomi',null=True, blank=True)
    icon = models.ImageField(upload_to='our_social_media/', verbose_name='icon file', null=True, blank=True)
    url = models.CharField(max_length=500,verbose_name="Ijtimoiy tarmoq urlini kiriting")
    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Ijtimoiy Tarmoqlarimiz'
        verbose_name_plural = 'Ijtimoiy Tarmoqlarimiz'