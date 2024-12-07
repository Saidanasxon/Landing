from django.db import models
from ckeditor.fields import RichTextField

class PlanHeader(models.Model):
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)

    class Meta:
        verbose_name = "plan header"

class Step(models.Model):
    icon = models.ImageField(verbose_name='step icon', upload_to='plan_step_icons/', null=True, blank=True)
    title_ru = RichTextField(verbose_name="step title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="step title en", null=True, blank=True)
    description_ru = RichTextField(verbose_name="step description ru", null=True, blank=True)
    description_en = RichTextField(verbose_name="step description en", null=True, blank=True)