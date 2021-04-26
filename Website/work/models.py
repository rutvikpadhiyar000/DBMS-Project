from django.db import models
from  client.models import client
# Create your models here.

class employee(models.Model):
    emp_ID = models.IntegerField(default=0, primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_post = models.CharField(max_length=100)
    emp_DOB = models.DateTimeField('date of birth')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    emp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    emp_address = models.CharField(max_length=200)
    emp_salary = models.IntegerField(default=0)

class freelancer(models.Model):
    ID = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
    DOB = models.DateTimeField('date of birth')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    payment = models.IntegerField(default=0)

class request(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    emp_assigned = models.ForeignKey(employee, on_delete=models.CASCADE)
    receive_date = models.DateTimeField('receive date')
    completion_date = models.DateTimeField('completion date')
    notes = models.CharField(max_length=500, null=True)