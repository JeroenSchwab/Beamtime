from django.contrib import admin

# Register your models here.
from .models import HourRegistrationModel #, Operators, Source

#admin.site.register(Operators)
#admin.site.register(Source)
admin.site.register(HourRegistrationModel)
