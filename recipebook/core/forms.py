from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from django.contrib.auth import get_user_model

class customerRegistrationForm(UserCreationForm):
    customer_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20, required=True)
    is_customer = forms.BooleanField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'customer_name', 'phone','is_customer']