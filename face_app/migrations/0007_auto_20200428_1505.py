# Generated by Django 2.2.5 on 2020-04-28 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0006_auto_20200427_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='city',
        ),
        migrations.RemoveField(
            model_name='uploadimage',
            name='state',
        ),
    ]