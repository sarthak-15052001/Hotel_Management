from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, DeleteView, ListView
from django.contrib.auth.views import LoginView, AuthenticationForm, LogoutView
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django .urls import reverse_lazy
from django.contrib import messages
from hotel.models import *
from django.db.models import Q




# Create your views here.

#<-----------------------------------------------------Myadmin Dashboard Template View Starts from here------------------------->

class IndexTemplateView(TemplateView):
    template_name = 'myadmin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_booking'] = Booking.objects.count()
        context['total_room'] = Room.objects.count()
        context['total_customer'] = User.objects.filter(is_active=True, is_staff=False).count()
        # context['total_customer'] = User.objects.exclude(is_staff=True).count()
        return context

#<--------------------------------------------------------Myadmin Profile View Starts from here--------------------------------->

class AdminProfile(UpdateView):
    model = User
    form_class = AdminProfileForm
    template_name = 'myadmin/profile.html'
    success_url = '/myadmin/'
    

#<-------------------------------------------------------Signup View Starts from here------------------------------------------->

class SignUpView(CreateView):
       form_class = SignupForm
       template_name = 'myadmin/signup.html'
       success_url = reverse_lazy("myadmin:userlogin")


#<---------------------------------------------------------User Login View Starts from here-------------------------------------->

class UserLogin(LoginView):
    Authentication_Form = UserLoginForm
    template_name = 'myadmin/login.html'


#<----------------------------------------------------------Logout View starts from here----------------------------------------->

class Logout(LogoutView):
    def get(self, request):
        logout(self.request)
        return redirect('myadmin:userlogin')


#<------------------------------------------------------------Room Details are starts here----------------------------------------->

class AdminRoomCreate(CreateView):
    model = Room
    form_class = AdminRoomForm
    template_name = 'myadmin/addroom.html'
    success_url = reverse_lazy('myadmin:roomlist')

    def form_valid(self, form):
        room_obj = form.save()
        ri = self.request.FILES.getlist('image')
        for f in ri:
            RoomImage.objects.update_or_create(image=f, room=room_obj)
            return super().form_valid(form)

#<--------------------------------Admin Room List View Start From here------------------------------------------------------------->

class AdminRoomList(ListView):
    model = Room
    template_name = 'myadmin/roomlist.html'

    # def get_queryset(self):
    #     queryset= super().get_queryset()
    #     room_category = self.request.GET.get('room_category')

    #     if room_category:
    #         queryset = queryset.filter(Q(room_categories__icontains=room_category))
    #     return queryset 

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search_query')

        if search_query:
            # Try to cast the search query to an integer (room number)
            try:
                room_no = int(search_query)
                queryset = queryset.filter(Q(room_no=room_no))
            except ValueError:
                # If it's not a valid integer, search by room category
                queryset = queryset.filter(Q(room_categories__icontains=search_query))

        return queryset

    

    


#<----------------------------------Admin Room Update View Start from here--------------------------->

class AdminRoomUpdateView(UpdateView):
    model = Room
    form_class = AdminRoomForm
    template_name = 'myadmin/updateroom.html'
    success_url = reverse_lazy('myadmin:roomlist')


    def form_valid(self, form):
        room_obj = form.save()
        ri = self.request.FILES.getlist('image')
        for f in ri:
            RoomImage.objects.update_or_create(image=f, room=room_obj)
            return super().form_valid(form)

#<-----------------------------------Admin Room Delete View start from here------------------------------>

class AdminRoomDeleteView(DeleteView):
    model = Room
    template_name = 'myadmin/deleteroom.html'
    success_url = reverse_lazy("myadmin:roomlist")

#<-----------------------------------Admin Customer List View Start from here----------------------------->

class AdminCustomerListView(ListView):
    model = User
    template_name = 'myadmin/customerdetail.html'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(is_superuser=False)
    #     return qs    

    def get_queryset(self):
        qs = super().get_queryset().filter(is_superuser=False)
        search_query = self.request.GET.get('search', None)

        if search_query:
            qs = qs.filter(
                Q(first_name__icontains=search_query) | 
                Q(phone_no__icontains=search_query) |
                Q(city__icontains=search_query) |
                Q(state__icontains=search_query)
            )
        return qs

#<------------------------------------Admin Customer Update view Starts from here----------------------------->

class AdmincustomerUpdateView(UpdateView):
    model = User
    form_class = AdminProfileForm
    template_name = 'myadmin/customerupdate.html'
    success_url = reverse_lazy("myadmin:customerlist")

#<----------------------------------------Admin Customer DeleteView Starts from here----------------------------->

class AdminCustomerDeleteView(DeleteView):
    model = User
    template_name = 'myadmin/customerdelete.html'
    success_url = reverse_lazy("myadmin:customerlist")

#<---------------------------------------------Admin Booking List View Starts from here--------------------------->

class AdminBookingList(ListView):
    model = Payment
    template_name = 'myadmin/adminbookinglist.html'

    def get_queryset(self):
      qs = self.request.GET.get('search', '')

      queryset = Payment.objects.filter(
        Q(user__first_name__icontains=qs) |
        Q(user__email__icontains=qs) |
        Q(user__phone_no__icontains=qs) |
        Q(booking__room__room_categories__icontains=qs) |
        Q(booking__room__room_no__icontains=qs)
      )
      return queryset


#<-----------------------------------------------------Admin Booking Invoice List Starts from here------------------------------>

class AdminBookingInvoiceList(ListView):
    model = Payment
    template_name = 'myadmin/adminbookinginvoice.html'

    def get_queryset(self):
      qs = self.request.GET.get('search', '')

      queryset = Payment.objects.filter(
        Q(user__first_name__icontains=qs) |
        Q(user__email__icontains=qs) |
        Q(user__phone_no__icontains=qs) |
        Q(booking__room__room_categories__icontains=qs) |
        Q(booking__room__room_no__icontains=qs)
      )
      return queryset