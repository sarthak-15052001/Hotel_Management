from django.db import models
from hotel.modelmanager import BaseModel
from datetime import datetime
from django.core.validators import MinValueValidator
from myadmin.models import *
import random
# Create your models here.

class Room(BaseModel):
    FREE_BREAKFAST = "FREEBREAKFAST"
    FREE_LUNCH = "FREE LUNCH"
    FREE_DINNER = "FREE DINNER"
    FREE_BREAKFAST_AND_DINNER = "FREE BREAKFAST AND DINNER"
    FREE_WELCOME_DRINK = "FREE WELCOME DRINK"
    NO_FREE_FOOD = "NO FREE FOOD"

    FOOD_CATEGORIES = (
        ('FREE BREAKFAST', FREE_BREAKFAST),
        ('FREE LUNCH', FREE_LUNCH),
        ('FREE DINNER', FREE_DINNER),
        ('FREE BREAKFAST AND DINNER', FREE_BREAKFAST_AND_DINNER),
        ('FREE WELCOME DRINK', FREE_WELCOME_DRINK),
        ('NO FREE FOOD', NO_FREE_FOOD)
    )

    PREMIUM_ROOM = "PREMIUM ROOM"
    PRESIDENTIAL_SUITE_POOL_VIEW = "PRESIDENTIAL SUITE POOL VIEW"
    DELUXE = "DELUXE"
    KING = "KING"
    LUXURY = "LUXURY"
    SUPERIOR = "SUPERIOR"

    ROOM_CATEGORIES = (
        ('PREMIUM_ROOM', PREMIUM_ROOM),
        ('PRESIDENTIAL SUITE POOL VIEW', PRESIDENTIAL_SUITE_POOL_VIEW),
        ('DELUXE', DELUXE),
        ('KING', KING),
        ('LUXURY', LUXURY),
        ('SUPERIOR', SUPERIOR)
    )

    KING = "KING"
    TWIN = "TWIN"
    QUEEN = "QUEEN"

    BED_CATEGORIES = (
        ('KING', KING),
        ('TWIN', TWIN),
        ('QUEEN', QUEEN)
    )

    AC_ROOM = "AC ROOM"
    NON_AC_ROOM = 'NON AC ROOM'

    ROOM_STOCK = (
        ('AC ROOM', AC_ROOM),
        ('NON AC ROOM', NON_AC_ROOM)
    )

    room_stock = models.CharField(max_length=50, choices=ROOM_STOCK)
    food_categgories = models.CharField(max_length=50, choices=FOOD_CATEGORIES)
    room_price = models.FloatField()
    #room_image = models.ImageField(upload_to='upload/', max_length=255, null=True, default=None)
    room_no = models.IntegerField()
    room_categories = models.CharField(max_length=30, choices=ROOM_CATEGORIES)
    bed_categories = models.CharField(max_length=20, choices=BED_CATEGORIES)
    capacity = models.IntegerField(validators=[MinValueValidator(1)]) 
    #is_available = models.CharField(max_length=30, default=True)
    


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomimage")
    image = models.FileField(upload_to='upload/', max_length=255, null=True, default=None)


class Booking(BaseModel):
    #date = models.DateField(null=True, default=datetime.now)
    check_in = models.DateField(null=True, default=datetime.now)
    check_out = models.DateField(null=True, default=datetime.now)

    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

    BOOKING_STATUS = (
        ('CONFIRMED', CONFIRMED),
        ("CANCELLED", CANCELLED)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_booking")
    total_members = models.IntegerField()
    booking_status = models.CharField(max_length=50, choices=BOOKING_STATUS)
    total_days = models.IntegerField(null=True)
    no_of_room = models.IntegerField()
    #total_amount = models. FloatField(null=True)
    #is_active = models.BooleanField(default=True)


    
class Payment(BaseModel):
    CARD = "CARD"
    CASH = "CASH"
    PAYTM = "PAYTM"

    PAYMENT_TYPE = {
        ('CARD', CARD),
        ('CASH', CASH),
        ('PAYTM', PAYTM),
    }

    payemnt_type = models.CharField(max_length=30, choices=PAYMENT_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    order_id = models.IntegerField(unique=True, null=True, default=None)
    made_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = random.randint(1000, 9999)
        super().save(*args, **kwargs)