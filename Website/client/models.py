from django.db import models

# Create your models here.

class client(models.Model):
    client_name = models.CharField(max_length=100, null=True)
    client_address = models.CharField(max_length=200)
    client_contact = models.CharField(max_length=10, default=None, null=True)

    def __str__(self):
        return self.client_name + " " + str(self.client_contact)