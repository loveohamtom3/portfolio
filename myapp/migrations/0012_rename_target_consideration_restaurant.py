# Generated by Django 4.1 on 2023-02-05 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_target_like_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consideration',
            old_name='target',
            new_name='restaurant',
        ),
    ]
