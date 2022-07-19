from django.http import HttpResponse
from django.shortcuts import render
from .models import Car
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'color']


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'
