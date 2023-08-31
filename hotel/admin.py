from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(RoomImage)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_no', 'room_categories', 'bed_categories', 'room_stock', 'capacity', 'room_price']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'room', 'check_in', 'check_out', 'total_members', 'no_of_room', 'total_days', 'booking_status']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'made_on', 'user', 'total_amount']