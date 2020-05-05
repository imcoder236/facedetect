# Generated by Django 2.2.5 on 2020-04-24 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ip_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('port', models.CharField(max_length=50)),
                ('strs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IPser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('port', models.CharField(max_length=50)),
                ('strs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='live_track_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='uploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]