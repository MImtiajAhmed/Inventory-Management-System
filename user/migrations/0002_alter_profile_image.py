# Generated by Django 4.0.6 on 2022-09-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='Profile_Images'),
        ),
    ]
