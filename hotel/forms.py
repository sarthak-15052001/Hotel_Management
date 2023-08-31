from django import forms
from .models import *


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'check_in',
            'check_out',
            'total_members',
            'total_days',
            'no_of_room',
        ]


class BookingPaymentForm(forms.ModelForm):
    class Meta:
         model = Payment
         fields = [
            'payemnt_type',
            'total_amount',
         ]

    def __init__(self, **kwargs):
        booking_id = kwargs.pop("booking_id")
        super().__init__(**kwargs)
        booking_obj = Booking.objects.get(id=booking_id)
        self.fields["total_amount"].initial = booking_obj.total_days * booking_obj.no_of_room * booking_obj.room.room_price