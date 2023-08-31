from django.urls import path
from myadmin import views


app_name="myadmin"

urlpatterns = [
    path('myadmin/', views.IndexTemplateView.as_view(), name="myadmin"),
    path('profile/<int:pk>', views.AdminProfile.as_view(), name="profile"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('userlogin/', views.UserLogin.as_view(), name="userlogin"),
    path('userlogout/', views.Logout.as_view(), name="userlogout"),
    path('addroom/', views.AdminRoomCreate.as_view(), name="addroom"),
    path('roomlist/', views.AdminRoomList.as_view(), name="roomlist"),
    path('updateroom/<int:pk>', views.AdminRoomUpdateView.as_view(), name="updateroom"),
    path('deleteroom/<int:pk>', views.AdminRoomDeleteView.as_view(), name="deleteroom"),
    path('customerlist/', views.AdminCustomerListView.as_view(), name="customerlist"),
    path('customerupdate/<int:pk>', views.AdmincustomerUpdateView.as_view(), name="customerupdate"),
    path('customerdelete/<int:pk>', views.AdminCustomerDeleteView.as_view(), name="customerdelete"),
    path('adminbookinglist/', views.AdminBookingList.as_view(), name="adminbookinglist"),
    path('admininvoice/', views.AdminBookingInvoiceList.as_view(), name="admininvoice"),
]
