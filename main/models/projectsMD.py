from django.db import models
from ckeditor.fields import RichTextField

class ProjectsHeader(models.Model):
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)

    class Meta:
        verbose_name = "Projects Header"

class Project(models.Model):
    title_ru = RichTextField(verbose_name="project title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="project title en", null=True, blank=True)
    subtitle_ru = RichTextField(verbose_name="project subtitle ru", null=True, blank=True)
    subtitle_en = RichTextField(verbose_name="project subtitle en", null=True, blank=True)
    description_ru = RichTextField(verbose_name="project description ru", null=True, blank=True)
    description_en = RichTextField(verbose_name="project description en", null=True, blank=True)
    photo = models.ImageField(upload_to="projects/", verbose_name="project photo", null=True, blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"