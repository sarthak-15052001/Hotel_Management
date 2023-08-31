# Generated by Django 4.2.3 on 2023-08-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0020_remove_room_is_available_alter_payment_payemnt_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payemnt_type',
            field=models.CharField(choices=[('CARD', 'CARD'), ('CASH', 'CASH'), ('PAYTM', 'PAYTM')], max_length=30),
        ),
    ]