# Generated by Django 4.0.5 on 2022-07-20 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfilesapp', '0012_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='foto',
        ),
    ]
