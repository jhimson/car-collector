from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Accessory, Car
from .forms import RacingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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


# def cars_detail(request, car_id):
#     car = Car.objects.get(id=car_id)
#     return render(request, 'cars/detail.html', {'car': car})
# update this view function
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    id_list = car.accessories.all().values_list('id')
    accessories_car_doesnt_have = Accessory.objects.exclude(id__in=id_list)
    racing_form = RacingForm()
    return render(request, 'cars/detail.html', {
        'car': car, 'racing_form': racing_form,
        'accessories': accessories_car_doesnt_have
    })


class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'color']

    success_url = '/cars/'


class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'color']


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'


def add_racing(request, car_id):
    # create a ModelForm instance using the data in request.POST
    form = RacingForm(request.POST)
    # validate the form
    if form.is_valid():
        new_racing = form.save(commit=False)
        new_racing.car_id = car_id
        new_racing.save()
    return redirect('detail', car_id=car_id)


class AccessoryList(ListView):
    model = Accessory


class AccessoryDetail(DetailView):
    model = Accessory


class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'


class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['name', 'color']


class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/cars/'


def assoc_accessory(request, car_id, accessory_id):
    Car.objects.get(id=car_id).accessories.add(accessory_id)
    return redirect('detail', car_id=car_id)
