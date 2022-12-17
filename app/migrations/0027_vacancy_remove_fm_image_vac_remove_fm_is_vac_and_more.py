# Generated by Django 4.1.3 on 2022-12-17 09:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_fm_vac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_vac', models.CharField(db_index=True, max_length=100, verbose_name='Title')),
                ('image_vac', models.ImageField(blank=True, upload_to='media/%Y/%m/%d', verbose_name='Photo Vacancy')),
                ('text_vac', ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True)),
                ('is_pub_vac', models.BooleanField(default=False, verbose_name='Published')),
                ('slug_vac', models.SlugField(blank=True, unique=True, verbose_name='URL')),
                ('added_vac', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('updated_vac', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
        ),
        migrations.RemoveField(
            model_name='fm',
            name='image_vac',
        ),
        migrations.RemoveField(
            model_name='fm',
            name='is_vac',
        ),
        migrations.RemoveField(
            model_name='fm',
            name='vac',
        ),
    ]
