from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Booking(models.Model):
    Name = models.CharField(max_length=200, null=False, blank=False)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Address = models.CharField(max_length=100, null=False, blank=False)
    Phone_number = models.CharField(max_length=200, null=False, blank=False)
    Khasara = models.IntegerField()
    Advisoryname = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.Name


class User(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)