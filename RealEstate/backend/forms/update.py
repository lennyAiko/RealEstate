from django.forms import ModelForm
from django import forms
from ..models import Client, Order, Property, Staff
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UpdateClient(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('registered_by')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        }


class UpdateStaff(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        }


class UpdateProperty(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of property'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location of property'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }


class UpdateOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount paid'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
            'lease_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lease period'}),
        }