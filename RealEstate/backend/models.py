from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Staff(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=60, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(null=True, default="default.png")
    password = models.CharField(null=True, blank=True, max_length=30)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ['-date_created']


class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=60, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(null=True, default="default.png")
    registered_by = models.CharField(null=True, blank=True, max_length=60)
    password = models.CharField(null=True, blank=True, max_length=30)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ['-date_created']


class Property(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.location}"

    class Meta:
        ordering = ['-date_created']
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class Order(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, null=True, on_delete=models.CASCADE)
    amount_paid = models.FloatField(blank=True, null=True)
    lease_period = models.CharField(blank=True, max_length=15, null=True)
    status1 = models.ImageField(null=True, blank=True)
    status2 = models.ImageField(null=True, blank=True)
    status3 = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.property.name} - {self.client.username}"

    class Meta:
        ordering = ['-date_created']

    def balance(self):
        return self.property.amount - self.amount_paid
