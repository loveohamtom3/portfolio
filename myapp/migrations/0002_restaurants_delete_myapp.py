# Generated by Django 4.1 on 2022-11-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='住所')),
                ('description', models.TextField(verbose_name='説明')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
            ],
        ),

    ]
