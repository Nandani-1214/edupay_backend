from django.db import models

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

    def __str__(self):
        return self.name

#vendor 

class Vendor(models.Model):
    vendorName = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    bankAccount = models.CharField(max_length=50, blank=True, null=True)
    ifsc = models.CharField(max_length=20, blank=True, null=True)

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

    def __str__(self):
        return self.name     
    
        