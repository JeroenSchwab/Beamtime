# Hours model
from django.db import models
from smart_selects.db_fields import ChainedForeignKey, ForeignKey

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from beamrequest.models import BeamRequestModel

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

#class Source(models.Model):
#	Name = models.CharField(max_length=50)

#	def __str__(self):
#		return self.Name

#class Operators(models.Model):
#	Name = models.CharField(max_length=50)

#	def __str__(self):
#		return self.Name


# Create your models here.
class HourRegistrationModel(models.Model):

	#days of week choices
	SELECT		= 'Select'
	MONDAY		= 'Monday'
	TUESDAY		= 'Tuesday'
	WEDNESDAY	= 'Wednesday'
	THURSDAY	= 'Thursday'
	FRIDAY		= 'Friday'
	SATURDAY	= 'Saturday'
	SUNDAY		= 'Sunday'

	DAY_CHOICES = [
		(SELECT, ('Select a day')),
		(MONDAY, ('Monday')),
		(TUESDAY, ('Tuesday')),
		(WEDNESDAY,  ('Wednesday')),
		(THURSDAY, ('Thursday')),
		(FRIDAY, ('Friday')),
		(SATURDAY, ('Saturday')),
		(SUNDAY, ('Sunday')),
	]

	#week choices (1 to 52)
	WEEK_CHOICES = [tuple([x,x]) for x in range(1,53)]

	# month choices (1 to 12)
	MONTH_CHOICES = [tuple([x,x]) for x in range(1,13)]

	# day choices (1 to 31)
#	DAY_CHOICES = [tuple([x,x]) for x in range(1,32)]

#	project_code = models.ForeignKey(BeamRequestModel, on_delete=models.CASCADE, blank=True, null=True)
#	Year = models.IntegerField(('year'), validators=[MinValueValidator(2020), max_value_current_year]) #models.DateField(blank = True, null=True)
	year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(2020), max_value_current_year])
#	month = models.IntegerField(choices=MONTH_CHOICES, default=current_month())
	week = models.IntegerField(choices=WEEK_CHOICES, default=current_week())
#	day = models.IntegerField(choices=DAY_CHOICES, default=current_day())
	day = models.CharField(max_length=25, choices=DAY_CHOICES, default='SELECT')
#	hours_requested = models.ForeignKey(CreateBeamRequestModel, on_delete=models.CASCADE, blank=True, null=True)
	hours_deliverd = models.PositiveIntegerField(default='0')
#	hours_deliverd = models.ForeignKey(BeamRequestModel, on_delete=models.CASCADE, blank=True, null=True)
	woak = models.PositiveIntegerField(default='0')
	planned = models.PositiveIntegerField(default='0')
	unused = models.PositiveIntegerField(default='0')
	development = models.PositiveIntegerField(default='0')
	calibration = models.PositiveIntegerField(default='0')
	general_error = models.PositiveIntegerField(default='0')
	rf_error = models.PositiveIntegerField(default='0')
	emc1_error = models.PositiveIntegerField(default='0')
	foeldi_error = models.PositiveIntegerField(default='0')
	cryo_error = models.PositiveIntegerField(default='0')
	other_error = models.PositiveIntegerField(default='0')
	notes = models.TextField(blank=True, null=True)

#	def __str__(self):
#		return self.project_code



	#Spent Time choices
#	SELECT			= 'Select'
#	WOAK			= 'Woak'
#	PLANNED			= 'Planned standby'
#	UNUSED			= 'Unused BOT hours'
#	DEVELOPMENT		= 'Beam development'
#	CALIBRATIONS	= 'Calibrations'
#	GENERAL_ERROR	= 'General error'
#	RF_ERROR		= 'RF error'
#	EMC1_ERROR		= 'EMC1 error'
#	FOELDI_ERROR	= 'Foeldi error'
#	CRYO_ERROR		= 'Cryogenics error'
#	OTHER_ERROR		= 'Other error'

#	SPENT_TIME_CHOICES = [
#		(SELECT, ('Select an option')),
#		(WOAK, ('Woak')),
#		(PLANNED, ('Planned standby')),
#		(UNUSED,  ('Unused BOT hours')),
#		(DEVELOPMENT, ('Beam development')),	
#		(CALIBRATIONS, ('Calibrations')),
#		(GENERAL_ERROR, ('General error')),
#		(RF_ERROR, ('RF error')),
#		(EMC1_ERROR, ('EMC1 error')),
#		(FOELDI_ERROR, ('Foeldi error')),
#		(CRYO_ERROR, ('Cryogenics error')),
#		(OTHER_ERROR, ('Other error')),
#	]
	


