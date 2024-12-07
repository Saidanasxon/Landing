from django.db import models
from ckeditor.fields import RichTextField

class AboutHeader(models.Model):
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)

    class Meta:
        verbose_name = "About Header"

class About(models.Model):
    text1_ru = RichTextField(verbose_name="about text1 ru", null=True, blank=True)
    text1_en = RichTextField(verbose_name="about text1 en", null=True, blank=True)
    text2_ru = RichTextField(verbose_name="about text2 ru", null=True, blank=True)
    text2_en = RichTextField(verbose_name="about text2 en", null=True, blank=True)
    image = models.ImageField(verbose_name="about image", upload_to="about_images/", null=True, blank=True)

class Faq(models.Model):
    question_ru = RichTextField(verbose_name="question ru", null=True, blank=True)
    question_en = RichTextField(verbose_name="question en", null=True, blank=True)
    answer_ru = RichTextField(verbose_name="answer ru", null=True, blank=True)
    answer_en = RichTextField(verbose_name="answer en", null=True, blank=True)
