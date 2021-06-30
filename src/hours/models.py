from django.db import models
from smart_selects.db_fields import ChainedForeignKey, ForeignKey
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from beamrequest.models import CreateBeamRequestModel

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def current_week():
    return datetime.date.today().isocalendar()[1]

class Operators(models.Model):
	Name = models.CharField(max_length=50)

	def __str__(self):
		return self.Name

class Monday(models.Model):
	#Sources choices
	SELECT = 'Select'
	CUSP = 'CUSP'
	AECR = 'AECR'
	SNG = 'SNG'

	SOURCE_CHOICES = [
		(SELECT, ('Select a source')),
		(CUSP, ('CUSP')),
		(AECR, ('AECR')),
		(SNG, ('SNG')),
	]

	#week choices (1 to 52)
	WEEK_CHOICES = [tuple([x,x]) for x in range(1,53)]

#	Year = models.ManyToManyField(HourRegistrationModel)
#	Year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(2020), max_value_current_year])
#	Week = models.IntegerField(choices=WEEK_CHOICES, default=current_week())
#	Week = models.ManyToManyField(HourRegistrationModel)
	Day_Shift = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift = models.CharField(max_length=50, blank = True, null=True)
	Beam = models.CharField(max_length=50, blank = True, null=True)
	Source = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Customer = models.CharField(max_length=50, blank = True, null=True)
	Prjoect_Code = models.CharField(max_length=50, blank = True, null=True)
	Scheduled_Hours = models.CharField(max_length=50, blank = True, null=True)
	Delivered_Hours = models.CharField(max_length=50, blank = True, null=True)
	No_Operators = models.CharField(max_length=50, blank = True, null=True)
	Notes = models.TextField(blank = True, null=True)

	def __str__(self):
		return self.Name

# Create your models here.
class HourRegistrationModel(models.Model):

	#Spent Time choices
	SELECT			= 'Select'
	WOAK			= 'Woak'
	PLANNED			= 'Planned standby'
	UNUSED			= 'Unused BOT hours'
	DEVELOPMENT		= 'Beam development'
	CALIBRATIONS	= 'Calibrations'
	GENERAL_ERROR	= 'General error'
	RF_ERROR		= 'RF error'
	EMC1_ERROR		= 'EMC1 error'
	FOELDI_ERROR	= 'Foeldi error'
	CRYO_ERROR		= 'Cryogenics error'
	OTHER_ERROR		= 'Other error'

	SPENT_TIME_CHOICES = [
		(SELECT, ('Select an option')),
		(WOAK, ('Woak')),
		(PLANNED, ('Planned standby')),
		(UNUSED,  ('Unused BOT hours')),
		(DEVELOPMENT, ('Beam development')),	
		(CALIBRATIONS, ('Calibrations')),
		(GENERAL_ERROR, ('General error')),
		(RF_ERROR, ('RF error')),
		(EMC1_ERROR, ('EMC1 error')),
		(FOELDI_ERROR, ('Foeldi error')),
		(CRYO_ERROR, ('Cryogenics error')),
		(OTHER_ERROR, ('Other error')),
	]

	#Sources choices
	SELECT = 'Select'
	CUSP = 'CUSP'
	AECR = 'AECR'
	SNG = 'SNG'

	SOURCE_CHOICES = [
		(SELECT, ('Select a source')),
		(CUSP, ('CUSP')),
		(AECR, ('AECR')),
		(SNG, ('SNG')),
	]

	#week choices (1 to 52)
	WEEK_CHOICES = [tuple([x,x]) for x in range(1,53)]

	#Year = models.IntegerField(('year'), validators=[MinValueValidator(2020), max_value_current_year]) #models.DateField(blank = True, null=True)
	Year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(2020), max_value_current_year])
	Week = models.IntegerField(choices=WEEK_CHOICES, default=current_week())
	Monday = models.ForeignKey(Monday, on_delete=models.CASCADE, blank = True, null=True)
	Day_Shift_Monday = models.CharField(max_length=50, blank = True, null=True)
	Day_Shift_Tuesday = models.CharField(max_length=50, blank = True, null=True)
	Day_Shift_Wednesday = models.CharField(max_length=50, blank = True, null=True)
	Day_Shift_Thursday = models.CharField(max_length=50, blank = True, null=True)
	Day_Shift_Friday = models.CharField(max_length=50, blank = True, null=True)
	Day_Shift_Saturday = models.CharField(max_length=50, blank = True, null=True)
	Day_Shift_Sunday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Monday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Tuesday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Wednesday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Thursday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Friday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Saturday = models.CharField(max_length=50, blank = True, null=True)
	Evening_Shift_Sunday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Monday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Tuesday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Wednesday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Thursday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Friday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Saturday = models.CharField(max_length=50, blank = True, null=True)
	Night_Shift_Sunday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Monday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Tuesday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Wednesday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Thursday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Friday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Saturday = models.CharField(max_length=50, blank = True, null=True)
	Beam_Sunday = models.CharField(max_length=50, blank = True, null=True)
	Source_Monday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Source_Tuesday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Source_Wednesday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Source_Thursday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Source_Friday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Source_Saterday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Source_Sunday = models.CharField(max_length=25, choices=SOURCE_CHOICES, default='SELECT')
	Customer = models.CharField(max_length=50, blank = True, null=True)
	Prjoect_Code = models.CharField(max_length=50, blank = True, null=True)
	Scheduled_Hours = models.CharField(max_length=50, blank = True, null=True)
	Delivered_Hours = models.CharField(max_length=50, blank = True, null=True)
	No_Operators = models.CharField(max_length=50, blank = True, null=True)
	Notes_Monday = models.TextField(blank = True, null=True)
	Notes_Tuesday = models.TextField(blank = True, null=True)
	Notes_Wednesday = models.TextField(blank = True, null=True)
	Notes_Thursday = models.TextField(blank = True, null=True)
	Notes_Friday = models.TextField(blank = True, null=True)
	Notes_Saturday = models.TextField(blank = True, null=True)

#	def __str__(self):
#		return self.Week




	


