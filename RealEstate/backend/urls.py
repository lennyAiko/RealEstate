from django.contrib import admin
from .views import *
from django.urls import path

#<siteurl>/register_staff_admin -- To register staffs.

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
]
