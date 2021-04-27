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

    def __str__(self):
        return str(self.emp_ID) + " " + self.emp_name

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

    def __str__(self):
        return str(self.ID) + " " + self.name

class clean_request(models.Model):
    client = models.ForeignKey(client, on_delete=models.CASCADE, null=True)
    emp_assigned = models.ForeignKey(employee, on_delete=models.SET_NULL, null=True)
    receive_date = models.DateTimeField('receive date')
    completion_date = models.DateTimeField('completion date', null=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        if self.completion_date != None:
            return str(self.pk) + " " + "Done"
        else:
            return str(self.pk) + " " + "Pending"