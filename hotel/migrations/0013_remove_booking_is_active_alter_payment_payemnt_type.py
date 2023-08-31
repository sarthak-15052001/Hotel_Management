# Generated by Django 4.2.3 on 2023-07-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_remove_booking_status_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payemnt_type',
            field=models.CharField(choices=[('PAYTM', 'PAYTM'), ('CASH', 'CASH'), ('CARD', 'CARD')], max_length=30),
        ),
    ]
