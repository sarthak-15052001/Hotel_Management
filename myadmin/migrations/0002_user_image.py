# Generated by Django 4.2.3 on 2023-08-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=None, max_length=255, null=True, upload_to='upload/'),
        ),
    ]