from django.db import models
from ckeditor.fields import RichTextField

class ContactHeader(models.Model):
    title_ru = RichTextField(verbose_name="header title ru", null=True, blank=True)
    title_en = RichTextField(verbose_name="header title en", null=True, blank=True)

    class Meta:
        verbose_name = "Contact Header"

class SendMessage(models.Model):
    """Xabar qoldirish"""
    name = models.CharField(max_length=50, verbose_name='Ism')
    phone_number = models.CharField(max_length=20, verbose_name='Telefon raqam')
    email = models.EmailField(max_length=50, verbose_name='Email', blank=True, null=True)
    message = models.TextField(verbose_name='Xabar')

    def __str__(self):
        return f'Xabar qoldirilgan {self.name}'

    class Meta:
        verbose_name = 'Xabarlar(Message)'
        verbose_name_plural = 'Xabarlar(Messages)'

