# Generated by Django 2.2.5 on 2020-05-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0015_auto_20200503_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_status_report',
            name='status',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]