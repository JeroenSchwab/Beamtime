from django.db import models
from smart_selects.db_fields import ChainedForeignKey

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
#from beamrequest.models import CreateBeamRequestModel, IonSpecies

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def current_month():
    return datetime.date.today().month

def current_day():
    return datetime.date.today().day

def current_week():
    return datetime.date.today().isocalendar()[1]

class IonSpecies(models.Model):
#	ionspecie = models.CharField(max_length=10)
	name = models.CharField(max_length=10)

	def __str__(self):
#		return self.ionspecie
		return self.name

class Energys(models.Model):
	ion_species = models.ForeignKey(IonSpecies, on_delete=models.CASCADE)
	name = models.CharField(max_length=10)

	def __str__(self):
#		return self.energy
		return self.name

#class BeamModel(models.Model):
#	Project_Code = models.ForeignKey(CreateBeamRequestModel, on_delete=models.CASCADE)
#	Hours = models.IntegerField(default='1')
#	Ion_Species = models.ForeignKey(IonSpecies, on_delete=models.CASCADE)
#	Energy = ChainedForeignKey(Energys, chained_field="Ion_Species", chained_model_field="Ion_Species",	show_all=False,	auto_choose=True)
#	Flux = models.CharField(max_length=50, blank = True, null = True)

#	def __str__(self):
#		return self.Name

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

		#week choices (1 to 52)
	WEEK_CHOICES = [tuple([x,x]) for x in range(1,53)]

	# month choices (1 to 12)
	MONTH_CHOICES = [tuple([x,x]) for x in range(1,13)]

	# day choices (1 to 31)
	DAY_CHOICES = [tuple([x,x]) for x in range(1,32)]

	#fields of the model
	project_code = models.CharField(unique=True, max_length=20, blank = True)
	pac_rate = models.CharField(max_length=10, blank = True)
	partrec_contact_name = models.CharField(max_length=50, blank = True)
	partrec_contact_email = models.EmailField(blank = True)
	previous_experiment = models.CharField(max_length=200, blank = True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='SELECT')
	project_title = models.CharField(max_length=100, blank = True)
	spokesperson_name = models.CharField(max_length=50, blank = True)
	spokesperson_adress = models.CharField(max_length=50, blank = True)
	spokesperson_phonenumber = models.CharField(max_length=20, blank = True)
	spokesperson_email = models.EmailField(blank = True)
	collaborator_name = models.TextField(blank = True)
	collaborator_nationality = models.TextField(blank = True)
	collaborator_home_institute = models.TextField(blank = True)
#	Different_Beams = models.IntegerField(choices=DIFBEAMS_CHOICES, default='1')
#	Shifts = models.IntegerField(choices=SHIFTS_CHOICES, default='1')
	beam_note = models.TextField(blank = True)
	hours_requested = models.IntegerField(default='1')
	ion_species = models.ForeignKey(IonSpecies, on_delete=models.CASCADE, blank = True, null=True)
	energy = ChainedForeignKey(Energys, chained_field="ion_species", chained_model_field="ion_species",	show_all=False,	auto_choose=True, blank = True, null=True)
	flux = models.CharField(max_length=50, blank = True, null = True)
	start_date = models.DateTimeField(blank = True, null=True)
	end_date = models.DateTimeField(blank = True, null=True)
	requiered_equipment = models.TextField(blank = True)
	special_requirements = models.TextField(blank = True)
	special_safety_procedures = models.TextField(blank = True)
	lab_support_requirements = models.TextField(blank = True)
	funded = models.TextField(blank = True)
	summary = models.TextField(blank = True)

#	year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(2020), max_value_current_year])
#	month = models.IntegerField(choices=MONTH_CHOICES, default=current_month())
#	week = models.IntegerField(choices=WEEK_CHOICES, default=current_week())
#	day = models.IntegerField(choices=DAY_CHOICES, default=current_day())
	hours_deliverd = models.PositiveIntegerField(default='0')#, blank=True, null=True
	woak = models.PositiveIntegerField(default='0')
	planned = models.PositiveIntegerField(default='0')
	unused = models.PositiveIntegerField(default='0')
	defelopment = models.PositiveIntegerField(default='0')
	calibration = models.PositiveIntegerField(default='0')
	general_error = models.PositiveIntegerField(default='0')
	rf_error = models.PositiveIntegerField(default='0')
	emc1_error = models.PositiveIntegerField(default='0')
	foeldi_error = models.PositiveIntegerField(default='0')
	cryo_error = models.PositiveIntegerField(default='0')
	other_error = models.PositiveIntegerField(default='0')
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.project_code

	def get_absolute_url(self):
		return f"/beamrequest/{self.project_code}"

	def get_edit_url(self):
		return f"{{self.get_absolute_url}}/update/"

	def get_delete_url(self):
#		return f"/beamrequest/{self.Project_Code}/delete/"
		return f"{{self.get_absolute_url}}/delete/"


#Ion_Species = models.ForeignKey(IonSpecies, on_delete=models.CASCADE)
#    Energy = ChainedForeignKey(Energys, chained_field="Ion_Species", chained_model_field="Ion_Species", show_all=False, auto_choose=True)