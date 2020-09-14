from django.forms import ModelForm
from django import forms
from ..models import Client, Order, Property, Staff
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterClient(UserCreationForm):
    password1 = forms.CharField(label='Enter Password',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        }


class RegisterClient(UserCreationForm):
    password1 = forms.CharField(label='Enter Password',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
        }


class RegisterProperty(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of property'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location of property'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }


class MakeOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount paid'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
            'lease_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lease period'}),
        }