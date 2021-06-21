from django.contrib import admin

# Register your models here.
from .models import CreateBeamRequestModel, IonSpecies, Energys

admin.site.register(CreateBeamRequestModel)
admin.site.register(IonSpecies)
admin.site.register(Energys)


