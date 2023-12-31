# Generated by Django 4.2.3 on 2023-07-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('room_stock', models.CharField(choices=[('AC ROOM', 'AC_ROOM'), ('NON AC ROOM', 'NON AC ROOM')], max_length=50)),
                ('food_categgories', models.CharField(choices=[('FREE BREAKFAST', 'FREEBREAKFAST'), ('FREE LUNCH', 'FREE LUNCH'), ('FREE DINNER', 'FREE DINNER'), ('FREE BREAKFAST AND DINNER', 'FREE BREAKFAST AND DINNER'), ('FREE WELCOME DRINK', 'FREE WELCOME DRINK'), ('NO FREE FOOD', 'NO FREE FOOD')], max_length=50)),
                ('room_price', models.FloatField()),
                ('room_image', models.ImageField(default=None, max_length=255, null=True, upload_to='upload/')),
                ('room_no', models.IntegerField()),
                ('room_categories', models.CharField(choices=[('PREMIUM_ROOM', 'PREMIUM ROOM'), ('PRESIDENTIAL SUITE POOL VIEW', 'PRESIDENTIAL SUITE POOL VIEW'), ('DELUXE', 'DELUXE'), ('KING', 'KING'), ('LUXURY', 'LUXURY'), ('SUPERIOR', 'SUPERIOR')], max_length=30)),
                ('bed_categories', models.CharField(choices=[('KING', 'KING'), ('TWIN', 'TWIN'), ('QUEEN', 'QUEEN')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
