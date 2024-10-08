from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)

class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    dob=models.DateField(max_length=50,null=True)
    age=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
    gender=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=50,null=True)
    last_donate_date=models.CharField(max_length=10,null=True)
class Blood_Donation(models.Model):
    public=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    # dob=models.DateTimeField(max_length=50,null=True)
    # age=models.CharField(max_length=50,null=True)
    dateofdonation=models.CharField(max_length=10,null=True)
    healthissue=models.CharField(max_length=50,null=True)
class Organ_Donation(models.Model):
    public=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    # WillingToDonate=models.CharField(max_length=10,null=True)
    PreviousOrganDonate=models.CharField(max_length=10,null=True)
    LastOrganDonationDate=models.CharField(max_length=50,null=True)
    CheckupDate=models.DateField(max_length=50,null=True)
    Organ=models.CharField(max_length=50,null=True)
    healthissue=models.CharField(max_length=50,null=True)
    hospitalname=models.CharField(max_length=75,null=True)
    status=models.CharField(max_length=20,null=True)
    checkupstatus=models.CharField(max_length=20,null=True)

class Pledge_Form(models.Model):
    fullName=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    medicalConditions=models.CharField(max_length=50,null=True)
    organPreferences=models.CharField(max_length=50,null=True)

class BloodBank(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True)

class BloodStocks(models.Model):
    user=models.ForeignKey(BloodBank,on_delete=models.CASCADE,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    availability=models.CharField(max_length=50,null=True)
