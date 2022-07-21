from pyexpat import model
from django.db import models
from django.urls import reverse
# Create your models here.


class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessory_detail', kwargs={'pk': self.id})


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=250)
    # Add the M:M relationship
    accessories = models.ManyToManyField(Accessory)

    # new code below
    def __str__(self):
        return self.make

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})


# Add new Feeding model below Cat model


class Racing(models.Model):
    date = models.DateField()
    location = models.TextField(
        max_length=100, default='123 South Street, Endicot NY 11219')

    # create a car_id column in the db
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    # change the default sort
    class Meta:
        ordering = ['-date']

    # def __str__(self):
    #     return f"Racing at {self.get_location_display()} on {self.date}"
