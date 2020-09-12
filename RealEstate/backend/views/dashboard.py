from ..models import *
from django.shortcuts import render

# Also holds views for profile

def dashboard(request):
    order = Order.objects.all()
    client = Client.objects.all()
    prop = Property.objects.all()

    total_order = order.count()
    total_client = client.count()
    total_prop = prop.count()

    context = {
        'total_order': total_order,
        'total_client': total_client,
        'total_prop': total_prop,
    }
    return render(request, 'staff/dashboard.html', context)