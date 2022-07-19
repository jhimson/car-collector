from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
# ! CONTROLLER
# Create your views here.

# Add the Cat class & list and view function below the imports


# class Car:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color


# cars = [
#     Car('Toyota', 'Mustang Mach-E', 'White'),
#     Car('Audi', 'V8', 'Blue'),
#     Car('BMW', 'X5 Sports', 'White')
# ]


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})
