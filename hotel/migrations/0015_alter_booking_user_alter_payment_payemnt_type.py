# Generated by Django 4.2.3 on 2023-07-31 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0014_alter_booking_room_alter_payment_payemnt_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payemnt_type',
            field=models.CharField(choices=[('CARD', 'CARD'), ('PAYTM', 'PAYTM'), ('CASH', 'CASH')], max_length=30),
        ),
    ]
