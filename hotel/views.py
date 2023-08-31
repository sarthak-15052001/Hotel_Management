from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView, DeleteView, ListView, View
from .models import *
from .forms import *
from myadmin.forms import *
from django.contrib import messages
import json
from datetime import timedelta
from django.http import JsonResponse
from hotel.service.mails import HotelBookedEmailSender
from hotel.utils import render_to_pdf
from math import ceil
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



# Create your views here.

#----------------------Index Template Starts from here-------------------------------->

class IndexTemplateView(TemplateView):
    template_name = 'hotel/index.html'


#----------------------------About Template Starts from here---------------------------->

class AboutTemplateView(TemplateView):
    template_name = 'hotel/about.html'

#------------------------------Our Room Template Starts from here------------------------->

class OurRoomTemplateView(TemplateView):
    template_name = 'hotel/our-room.html'

#------------------------------Gallery Template View Starts from here----------------------->

class GalleryTemplateView(TemplateView):
    template_name = 'hotel/gallery.html'

#----------------------------------Blog Template View Starts from here---------------------->

class BlogTemplateView(TemplateView):
    template_name = 'hotel/blog.html'

#---------------------------------Contact Template View Starts from here-------------------->

class ContactUsTemplateView(TemplateView):
    template_name = 'hotel/contact-us.html'

#<--------------------------------------------Customer Profile View Starts From here----------------------->

class CustomerProfileDetailView(DetailView):
    model = User
    template_name = 'hotel/customerprofile.html'


#<----------------------------------------------Customer Update Profile View Starts from here----------------------->

class CustomerProfileUpdateView(UpdateView):
    model = User
    form_class = AdminProfileForm
    template_name = 'hotel/updateprofile.html'
    success_url = reverse_lazy('hotel:customerprofile')

#<----------------------------------------------Room Image List View Starts from here----------------------------->

class RoomImageListView(ListView):
    model = Room
    template_name = 'hotel/roomimagelist.html'

    def get(self, request):
        check_in = request.GET.get("check_in")
        check_out = request.GET.get("check_out")
        total_members = request.GET.get("total_members")

        if  check_in == None or check_out == None:
            return render(request, self.template_name)

        unavailable_rooms = Room.objects.filter(room_booking__booking_status=Booking.CONFIRMED).filter(Q(room_booking__check_in__lte=check_out, room_booking__check_out__gte=check_in) | Q(room_booking__check_in__gte=check_in, room_booking__check_out__lte=check_out))

        booked_room_ids = unavailable_rooms.values_list('id', flat=True)

        available_rooms = Room.objects.exclude(id__in = booked_room_ids)

        return render(request, self.template_name, {"available_rooms": available_rooms, "check_in": check_in, "check_out": check_out, "total_members": total_members})
    

#<---------------------------------------------------Room Detail View Starts from here------------------------------> 

class RoomDetailView(DetailView):
    model = Room
    template_name = 'hotel/roomdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.kwargs
        room_id = data["pk"]
        post = RoomImage.objects.filter(room=room_id) 
        context["post"] = post
        context["check_in"] = self.request.GET["check_in"]
        context["check_out"] = self.request.GET["check_out"]
        context["total_members"] = self.request.GET["total_members"]
        room = Room.objects.get(id=room_id)
        no_of_room = int(context["total_members"])/int(room.capacity)
        context["no_of_room"] = ceil(no_of_room)
        room_price = room.room_price
        total_room_price = int(room_price) * int(context["no_of_room"])
        context["total_room_price"] = total_room_price
        return context
    

#<-----------------------------------Booking Create View Starts from here---------------------------------->

class BookingCreateView(CreateView):
    form_class = BookingForm
    template_name = 'hotel/bookingroom.html'
    #success_url = reverse_lazy('hotel:bookingpayment')

    def form_valid(self, form):
        booking = form.save(commit=False)
        room = Room.objects.get(id=self.kwargs['id'])
        booking.room = room
        booking.user = self.request.user
        booking.save()
        room.is_available = False
        room.save()
        return redirect(reverse("hotel:bookingpayment", kwargs={"pk":booking.id}))

  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.kwargs
        room_id = data['id']
        room_data = Room.objects.get(id=room_id)
        room_image = RoomImage.objects.filter(room=room_id)
        # room_booking_dates = Booking.objects.filter(room=room_data)
        ins = self.request.GET["check_in"]
        out = self.request.GET["check_out"]
        context["check_in"] = ins
        context["check_out"]= out
        context["total_members"] = self.request.GET["total_members"]
        check_ins = datetime.strptime(ins, "%Y-%m-%d")
        check_outs = datetime.strptime(out, "%Y-%m-%d")
        days = (check_outs - check_ins).days
        context["total_days"] = days
        context["no_of_room"] = self.request.GET["no_of_room"]

        # disable_date = []
        # for booking in room_booking_dates:

        #     def daterange(date1, date2):
        #         for n in range(int ((date2 -date1).days)+1):
        #             yield date1 + timedelta(n)

        #     for dt in daterange(booking.check_in, booking.check_out):
        #         disable_date.append(dt.strftime("%d/%m/%Y"))
        # print(disable_date)

        context['room_image'] = room_image
        context['room_id'] = room_id
        context['room_data'] = room_data
        # context["disable_date"] = disable_date
        return context

#<-----------------------------------------Booking List View Starts from here----------------------------->

class BookingListView(ListView):
    model = Booking
    template_name = 'hotel/bookinglist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.pk
        bookings = Booking.objects.filter(user=user).annotate(total_amount=Sum('payment__total_amount'))
        # for booking in bookings:
        #     total = Payment.objects.get(user=user, booking=booking)
        #     booking.total_amount = total.total_amount
        context['post'] = bookings 
        return context
    

                                                                                                                      

#<-------------------------------------------Booking Cancel View Starts fromn here-------------------------->

class BookingCancelView(View):

     def post(self, request):
        booking_id = request.POST.get('pk')
        try:
            booking = Booking.objects.get(id=booking_id)
            if booking.booking_status == 'CONFIRMED':
                booking.booking_status = "CANCELLED"
                booking.save()
                return JsonResponse({"status": "success", "new_status": booking.booking_status})
            else:
                return JsonResponse({"status": "error", "message": "Booking cannot be cancelled."})
        except Booking.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Booking not found."})
    
    

#<-----------------------------------------Payment Form Create vuew starts from here----------------------->

class PaymentCreateView(CreateView):
    model = Payment
    form_class = BookingPaymentForm
    template_name = 'hotel/bookingpayment.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["booking_id"] = self.kwargs["pk"]
        return kwargs

    def form_valid(self, form):
        payment = form.save(commit=False)
        booking = Booking.objects.get(pk = self.kwargs['pk'])
        payment.booking = booking
        payment.user = self.request.user
        booking.booking_status = "CONFIRMED"
        booking.save()
        payment.save()
        # messages.success(self.request, 'Payment successful !!!!')

        #<-------------Email sends Logic Starts from here-------------------->
        username = self.request.user.username
        username = username.upper()
        subject = "Booking & Payment Confirmation"
        message = "Dear customer your booking has been confirmed."
        from_email = "admin@example.com"
        to_email = [self.request.user.email]
        variable_dict = {"username": username, "message": message}
        HotelBookedEmailSender().send_email_custom(subject, from_email, to_email, variable_dict)
        return redirect(reverse("hotel:bookinginvoice", kwargs={"pk":booking.pk}))


#<-----------------------------------------------------Booking Invoice List Starts from her------------------------------------>

class BookingInvoiceList(ListView):
    model = Payment
    template_name = 'hotel/bookinginvoice.html'

    # def get_queryset(self):
    #     queryset = Payment.objects.filter(user = self.request.user)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        context['object_list'] = Payment.objects.filter(booking__pk=id) 
        return context
    
    
#<--------------------------------------------------Booking Invoice PDF Generate View Starts from here----------------------------->

class GeneratePdf(View):
    model = Payment
    template_name = 'pdf/invoice.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs["pk"]
        payment = Payment.objects.filter(id=id)
        data = {
            'payment': payment,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')