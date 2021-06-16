from django.db import models
from smart_selects.db_fields import ForeignKey
from beamrequest.models import CreateBeamRequestModel

# Create your models here.
class Add_file_model(models.Model):
    file = models.FileField()
    Project_Id = models.ForeignKey(CreateBeamRequestModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Project_Id