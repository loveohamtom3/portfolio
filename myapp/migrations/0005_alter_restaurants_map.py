# Generated by Django 4.1 on 2023-01-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_consideration_footprint_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='map',
            field=models.URLField(max_length=1000, verbose_name='地図'),
        ),
    ]
