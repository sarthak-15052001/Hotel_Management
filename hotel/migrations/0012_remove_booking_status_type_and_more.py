# Generated by Django 4.2.3 on 2023-07-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_booking_is_active_alter_payment_payemnt_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status_type',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_amount',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payemnt_type',
            field=models.CharField(choices=[('PAYTM', 'PAYTM'), ('CARD', 'CARD'), ('CASH', 'CASH')], max_length=30),
        ),
    ]