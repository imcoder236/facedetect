# Generated by Django 2.2.5 on 2020-05-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0014_auto_20200503_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_status_report',
            name='in_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ip_status_report',
            name='out_time',
            field=models.DateTimeField(null=True),
        ),
    ]
