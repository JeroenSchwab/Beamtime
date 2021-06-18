from django.db import models
from smart_selects.db_fields import ForeignKey
from beamrequest.models import CreateBeamRequestModel

def generate_path(self, filename):
    url = "files/users/%s/%s" % (self.user.username, filename)
    url = '{0}/{1}'.format(instance.CreateBeamRequestModel.Project_Code, filename) #"pacnumber/%s" % (filename)
    return url

# Create your models here.
class Add_file_model(models.Model):
    Project_Code = models.ForeignKey(CreateBeamRequestModel, on_delete=models.CASCADE)
    file = models.FileField() #upload_to=generate_path
    def __str__(self):
#        return self.Project_Id, self.file
        return self.Project_Code, self.file





#class UserFiles(models.Model):
#    user = models.OneToOneField(User)
#    file = models.FileField(upload_to=generate_filename)