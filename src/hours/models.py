from django.db import models



# Create your models here.
class HourRegistration(models.Model):

	Spent_Time choices
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

	Year = models.DateField(blank = True, null=True)
	Week = models.DateField(blank = True, null=True)
	Day = 
	Day_Shift = 
	Evening_shift = 
	Night_Shift = 
	Beam = 
	Source = 
	Customer = 
	Prjoect_Code = 
	Scheduled_Hours = 
	Delivered_Hours = 
	No_Operators = 
	Notes_Monday
	Notes_Tuesday
	Notes_Wednesday
	Notes_Thursday
	Notes_Friday
	Notes_Saturday
	Woak, Planned standby, Unused BOT hours, Beam development, Calibrations, Error general, Error RF, Error EMC1, Error foeldi, Error cryo


