from django.forms import ModelForm
from django import forms
from ..models import Client, Order, Property, Staff
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SendEmail(forms.Form):
    email = forms.EmailField(label='Enter email',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    subject = forms.CharField(label='Enter Subject',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'})
                              )
    message = forms.CharField(label='Enter message',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter message'}))

    class Meta:
        fields = ['email', 'subject', 'message', ]


class SendMultiMail(forms.Form):
    subject = forms.CharField(label='Enter Subject',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}))
    message = forms.CharField(label='Enter message',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter message'}))
    
    class Meta:
        fields = ['subject', 'message', ]
