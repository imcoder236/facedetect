# Generated by Django 2.2.5 on 2020-05-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0020_passwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwd',
            name='user_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
