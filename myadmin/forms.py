from django import forms
from myadmin.models import User
from django.contrib.auth.forms import UserCreationForm
from hotel.models import *

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=70, required=False)
    last_name = forms.CharField(max_length=70, required=False)
    email = forms.EmailField(max_length=70, help_text="Enter a valid email address")
    phone_no = forms.CharField(max_length=70, help_text="Enter a valid phone No")
    username = forms.CharField(max_length=70, required=False)
    

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_no',
            'password1',
            'password2',
            'gender',
            'birth_date',
            'address',
            'street',
            'city',
            'state',
            'country',
            'pin_code',
        ]
        widgets = {
            "birth_date":forms.DateInput(attrs={'type':'date'}),               
        }


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=70, required=True, widget=forms.TextInput)
    password = forms.CharField(max_length=70, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']



class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_no',
            'gender',
            'birth_date',
            'address',
            'city',
            'state',
            'pin_code',
            'country',
            'image',
        ]
 
        widgets = {
            "birth_date": forms.DateInput(attrs={'type':'date'}),
        }

class AdminRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['is_available']