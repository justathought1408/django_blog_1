# Generated by Django 4.1.3 on 2022-12-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_vacancy_remove_fm_image_vac_remove_fm_is_vac_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='is_pub_vac',
            field=models.BooleanField(default=False, verbose_name='Vacancy Published'),
        ),
    ]
