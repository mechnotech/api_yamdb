# Generated by Django 3.0.5 on 2020-10-28 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1, message='Не меньше 1'), django.core.validators.MaxValueValidator(10, message='Не больше 10')], verbose_name='Оценка от 1 до 10'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Год'),
        ),
    ]