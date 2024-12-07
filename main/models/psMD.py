from django.db import models
from ckeditor.fields import RichTextField

class PSHeader(models.Model):
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)
    icon = models.ImageField(verbose_name='ps icon', upload_to='ps_icons/', null=True, blank=True)

    class Meta:
        verbose_name = "problem&solution header"

class Problem(models.Model):
    title_ru = RichTextField(verbose_name="muammo rus", null=True, blank=True)
    title_en = RichTextField(verbose_name="muammo eng", null=True, blank=True)

    def __str__(self):
        return self.title_en
    
class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name="problem", related_name="solutions")
    solution_ru = RichTextField(verbose_name="yechim rus", null=True, blank=True)
    solution_en = RichTextField(verbose_name="yechim eng", null=True, blank=True)

