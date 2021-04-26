from django.db import models

# Create your models here.

class client(models.Model):
    client_name = models.CharField(max_length=100)
    client_occupation = models.CharField(max_length=100)
    client_DOB = models.DateTimeField('date of birth')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    client_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    client_address = models.CharField(max_length=200)
