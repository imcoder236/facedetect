# Generated by Django 2.2.5 on 2020-04-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_app', '0005_city_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='aadharno',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='pincode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
