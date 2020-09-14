from ..models import *
from ..forms import *
from ..functions import *
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory


def registerClient(request):
    form = RegisterClient()
    if request.method == "POST":
        form = RegisterClient(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            data = form.cleaned_data
            group = Group.objects.get(name='client')
            user.groups.add(group)
            newClient = Client(user=user, **data, registered_by=staff)
            newClient.save()
            mail(email, username, password)
            return redirect('done')
    context = {'form': form}
    return render(request, 'staff/register.html', context)


def registerStaff(request):
    form = RegisterStaff()
    if request.method == "POST":
        form = RegisterStaff(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            data = form.cleaned_data
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            newStaff = Staff(user=user, **data, registered_by=staff)
            newStaff.save()
            mail(email, username, password)
            return redirect('done')
    context = {'form': form}
    return render(request, 'staff/register.html', context)


def registerProperty(request):
    form = RegisterProperty()
    if request.method == "POST":
        form = RegisterProperty(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prop = Property(**data)
            prop.save()
            return redirect('done')
    context = {'form': form}
    return render(request, 'staff/register.html', context)


def makeOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Client,
        Order,
        fields=('property', 'amount_paid', 'balance', 'lease_period',
                'status1', 'status2', 'status3'),
        extra=1,
        widgets={
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount paid'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
            'lease_period': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lease period'}),
        }
    )
    client = Client.objects.get(id=pk)
    form = Orderform(queryset=Order.objects.none(), instance=client)
    if request.method == 'POST':
        form = OrderFormSet(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('done')

    context = {'form': form}
    return render(request, 'staff/register.html', context)
