from django.db import models
from ckeditor.fields import RichTextField

class AchievementsHeader(models.Model):
    title_uz = RichTextField(verbose_name="header title uz")
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)
    class Meta:
        verbose_name = "achievements header"

class Achievement(models.Model):
    quantity = RichTextField(verbose_name="achievment soni")
    title_uz = RichTextField(verbose_name="achievment nomi uz")
    title_ru = RichTextField(verbose_name="achievment nomi ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="achievment nomi en", null=True, blank=True)

    class Meta:
        verbose_name = "achievment"