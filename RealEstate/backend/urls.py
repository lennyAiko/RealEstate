from django.contrib import admin
from .views import *
from django.urls import path

#<siteurl>/register_staff_admin -- To register staffs.

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("done/", done, name="done"),

    path("register_client/", registerClient, name="register_client"),
    path("register_staff/", registerStaff, name="register_staff"),
    path("register_property/", registerProperty, name="register_property"),
    path("make_order/", makeOrder, name="make_order"),
]
