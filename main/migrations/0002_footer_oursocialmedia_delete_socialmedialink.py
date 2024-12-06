# Generated by Django 5.1.2 on 2024-12-05 18:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_uz', ckeditor.fields.RichTextField(verbose_name='Footer matni uz')),
                ('description_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Footer matni ru')),
                ('description_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Footer matni en')),
                ('copyright_text_uz', ckeditor.fields.RichTextField(verbose_name='Copyrigth text uz')),
                ('copyright_text_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Copyrigth text ru')),
                ('copyright_text_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Copyrigth text en')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footerlar',
            },
        ),
        migrations.CreateModel(
            name='OurSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ijtimoiy tarmoq nomi')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='our_social_media/', verbose_name='icon file')),
                ('url', models.CharField(max_length=500, verbose_name='Ijtimoiy tarmoq urlini kiriting')),
            ],
            options={
                'verbose_name': 'Ijtimoiy Tarmoqlarimiz',
                'verbose_name_plural': 'Ijtimoiy Tarmoqlarimiz',
            },
        ),
        migrations.DeleteModel(
            name='SocialMediaLink',
        ),
    ]
