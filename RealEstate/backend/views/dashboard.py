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
    recent_order = Order.objects.all().last()

    context = {
        'total_order': total_order,
        'total_client': total_client,
        'total_prop': total_prop,
        'recent_order': recent_order,
    }
    return render(request, 'staff/dashboard.html', context)


def done(request):
    return render(request, 'staff/done.html')