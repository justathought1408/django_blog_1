# Generated by Django 4.1.3 on 2022-12-17 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_fm_vac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fm',
            name='vac',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Vacancy'),
        ),
    ]