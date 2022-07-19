from django.http import HttpResponse
from django.shortcuts import render
# ! CONTROLLER
# Create your views here.

# Add the Cat class & list and view function below the imports


class Car:  # Note that parens are optional if not inheriting from another class
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color


cars = [
    Car('Toyota', 'Mustang Mach-E', 'White'),
    Car('Audi', 'V8', 'Blue'),
    Car('BMW', 'X5 Sports', 'White')
]


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})
