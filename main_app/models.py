from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=250)

    # new code below
    def __str__(self):
        return self.make

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
