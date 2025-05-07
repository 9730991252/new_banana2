from django.db import models
from month.models import MonthField
# Create your models here.
class Sunil(models.Model):
    sum = models.IntegerField()

class Shope(models.Model):
    shope_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    contact_details = models.CharField(max_length=500, null=True)
    pin = models.IntegerField()
    edit_pin = models.IntegerField(default=1234)
    status = models.IntegerField(default=1)
    
class Shope_payment(models.Model):
    shope = models.ForeignKey(Shope, on_delete=models.CASCADE)
    amount = models.FloatField()
    from_date = models.DateField()
    to_date = models.DateField()
    payment_type = models.CharField(max_length=100)
    added_date = models.DateField(auto_now_add=True)
    
class Auto_Shope_payment(models.Model):
    shope = models.ForeignKey(Shope, on_delete=models.CASCADE)
    amount = models.FloatField()
    month = MonthField("Month Value", help_text="some help...")
    added_date = models.DateField(auto_now_add=True)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    is_paid = models.BooleanField(default=False) 