from django.db import models
from django.utils import timezone

# Create your models here.
# Admin login model 

class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    from django.db import models


#student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    division = models.CharField(max_length=20)
    roll = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20, blank=True, null=True)
    rfid = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.name

#vendor 

from django.db import models

class Vendor(models.Model):

    CATEGORY_CHOICES = [
        ('Stationary', 'Stationary'),
        ('Laundry', 'Laundry'),
        ('Printing', 'Printing'),
        ('Canteen', 'Canteen'),
    ]

    vendorName = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Stationary")

    password = models.CharField(max_length=100, null=True, blank=True)

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.vendorName

#parent model 

class Parent(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="parents"
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    relation = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=50, default="Admin")

    def __str__(self):
        return self.name     
    
#add-money 

class Wallet(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    rfid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.FloatField(default=0)
    


    def __str__(self):
        return self.student
    
    
class Transaction(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    rfid = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=20, default="credit")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.student
    
#vendor login
class VendorLogin(models.Model):

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)

    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.vendor)