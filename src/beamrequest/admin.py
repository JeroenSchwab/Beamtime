from django.contrib import admin

# Register your models here.
from .models import BeamRequestModel, IonSpecies, Energys

admin.site.register(BeamRequestModel)
admin.site.register(IonSpecies)
admin.site.register(Energys)


