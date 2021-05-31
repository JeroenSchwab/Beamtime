from django.db import models

class IonSpecies(models.Model):
	ionspecie = models.CharField(max_length=10)

	def __str__(self):
		return self.ionspecie


class Energys(models.Model):
	Ion_Species = models.ForeignKey(IonSpecies, on_delete=models.CASCADE)
	energy = models.CharField(max_length=50)

	def __str__(self):
		return self.energy
		
# Create your models here.
class CreateBeamRequestModel(models.Model):

	#status choices
	SELECT		= 'Select'
	REQUEST		= 'Request'
	TENTATIVE	= 'Tentavive'
	ACCEPTED	= 'Accepted'
	CONFIRMED	= 'Confirmed'
	CANCELLED	= 'Cancelled'
	COMPLETED	= 'Completed'
	QUEUED		= 'Queued'

	STATUS_CHOICES = [
		(SELECT, ('Select an option')),
		(REQUEST, ('Request')),
		(TENTATIVE, ('Tentative')),
		(ACCEPTED,  ('Accepted')),
		(CONFIRMED, ('Confirmed')),
		(CANCELLED, ('Cancelled')),
		(COMPLETED, ('Completed')),
		(QUEUED, ('Queued')),
	]

    #different beam choices (1 to 4)
	DIFBEAMS_CHOICES = [tuple([x,x]) for x in range(1,5)]

	#shift choices (1 to 16 is max a week)
	SHIFTS_CHOICES = [tuple([x,x]) for x in range(1,17)]



	#fields of the model
	Project_Code = models.CharField(unique=True, max_length=20, blank = True)
	Pac_Rate = models.CharField(max_length=10, blank = True)
	Partrec_Contact_Name = models.CharField(max_length=50, blank = True)
	Partrec_Contact_Email = models.EmailField(blank = True)
	Previous_Experiment = models.CharField(max_length=200, blank = True)
	Status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='SELECT')
	Project_Title = models.CharField(max_length=100, blank = True)
	Spokesperson_Name = models.CharField(max_length=50, blank = True)
	Spokesperson_Adress = models.CharField(max_length=50, blank = True)
	Spokesperson_Phonenumber = models.CharField(max_length=20, blank = True)
	Spokesperson_Email = models.EmailField(blank = True)
	Collaborator_Name = models.TextField(blank = True)
	Collaborator_Nationality = models.TextField(blank = True)
	Collaborator_Home_Institute = models.TextField(blank = True)
	Different_Beams = models.IntegerField(choices=DIFBEAMS_CHOICES, default='1')
	Shifts = models.IntegerField(choices=SHIFTS_CHOICES, default='1')
#	Ion_Species = models.CharField(max_length=20, choices=ION_CHOICES, default='H')
#	Energy = models.CharField(max_length=20, choices=ION_ENERGY_CHOICES, default='SELECT')
	Ion_Species = models.ForeignKey(IonSpecies, on_delete=models.SET_NULL, null=True)
	Energy = models.ForeignKey(Energys, on_delete=models.SET_NULL, null=True)
	Flux = models.CharField(max_length=20, blank = True)
	Start_Date = models.DateTimeField(blank = True)
	End_Date = models.DateTimeField(blank = True)
	Requiered_Equipment = models.TextField(blank = True)
	Special_Requirements = models.TextField(blank = True)
	Special_Safety_Procedures = models.TextField(blank = True)
	Lab_Support_Requirements = models.TextField(blank = True)
	Funded = models.CharField(max_length=20, blank = True)
	Summary = models.TextField(blank = True)

