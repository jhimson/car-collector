from django.contrib import admin

# Register your models here.
from .models import Car, Racing, Accessory
admin.site.register(Car)
admin.site.register(Racing)
admin.site.register(Accessory)
