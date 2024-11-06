from django.db import models


# Create your models here.
class Costumer(models.Model):
    fio = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    dob = models.DateField()
    dt = models.TimeField(auto_now_add=True)
