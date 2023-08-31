from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = (
        ('MALE', MALE),
        ('FEMALE', FEMALE)
    )

    gender = models.CharField(max_length=70, choices=GENDER_CHOICES, null=True, blank=True)
    phone_no = models.CharField(max_length=70, null=True, blank=True)
    street = models.CharField(max_length=70, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=70, null=True, blank=True)
    city = models.CharField(max_length=70, null=True, blank=True)
    state = models.CharField(max_length=70, null=True, blank=True)
    pin_code = models.CharField(max_length=70, null=True, blank=True)
    country = models.CharField(max_length=70, null=True, blank=True)
    image = models.ImageField(upload_to='upload/', max_length=255, null=True, default=None)