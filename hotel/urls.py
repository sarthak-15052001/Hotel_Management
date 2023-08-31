from django.urls import path
from hotel import views

app_name='hotel'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name="index"),
    path('about/', views.AboutTemplateView.as_view(), name="about"),
    path('ourroom/', views.OurRoomTemplateView.as_view(), name="ourroom"),
    path('gallery/', views.GalleryTemplateView.as_view(), name="gallery"),
    path('blog/', views.BlogTemplateView.as_view(), name="blog"),
    path('contact/', views.ContactUsTemplateView.as_view(), name="contact"),
    path('customerprofile/<int:pk>', views.CustomerProfileDetailView.as_view(), name="customerprofile"),
    path('updateprofile/<int:pk>', views.CustomerProfileUpdateView.as_view(), name="updateprofile"),
    path('room/', views.RoomImageListView.as_view(), name="room"),
    path('roomdetail/<int:pk>', views.RoomDetailView.as_view(), name="roomdetail"),
    path('bookingroom/<int:id>', views.BookingCreateView.as_view(), name="bookingroom"),
    path('bookinglist/', views.BookingListView.as_view(), name="bookinglist"),
    path('bookingcancel/', views.BookingCancelView.as_view(), name="bookingcancel"),
    path('bookingpayment/<int:pk>', views.PaymentCreateView.as_view(), name="bookingpayment"),
    path('bookinginvoice/<int:pk>', views.BookingInvoiceList.as_view(), name="bookinginvoice"),
    path('generatepdf/<int:pk>', views.GeneratePdf.as_view(), name="generatepdf"),
    #path('roomsearch/', views.RoomSearchView.as_view(), name="roomsearch"),
]
