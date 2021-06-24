from django.contrib import admin

# Register your models here.
from .models import HourRegistrationModel, Operators

admin.site.register(Operators)
admin.site.register(HourRegistrationModel)