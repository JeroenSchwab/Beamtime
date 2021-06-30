from django import forms
from django.forms import TextInput

# validation errors for dates
from django.core.exceptions import ValidationError

#import the date/time picker
#from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

#import my models
from .models import HourRegistrationModel, Monday

class Monday(forms.ModelForm):
	
	class Meta:
		model = Monday

		fields = [
#			'Year',
#			'Week',
			'Day_Shift',
			'Evening_Shift',
			'Night_Shift',
			'Beam',
			'Source',
			'Customer',
			'Prjoect_Code',
			'Scheduled_Hours',
			'Delivered_Hours',
			'No_Operators',
			'Notes',
		]
			
		
#creating a form
class HourRegistrationForm(forms.ModelForm):

	# create meta class
	class Meta:

		# specify model to be used
		model = HourRegistrationModel

		# specify fields to be used
		fields = [
			'Year',
			'Week',
			'Monday',
			'Day_Shift_Monday',
			'Day_Shift_Tuesday',
			'Day_Shift_Wednesday',
			'Day_Shift_Thursday',
			'Day_Shift_Friday',
			'Day_Shift_Saturday',
			'Day_Shift_Sunday',
			'Evening_Shift_Monday',
			'Evening_Shift_Tuesday',
			'Evening_Shift_Wednesday',
			'Evening_Shift_Thursday',
			'Evening_Shift_Friday',
			'Evening_Shift_Saturday',
			'Evening_Shift_Sunday',
			'Night_Shift_Monday',
			'Night_Shift_Tuesday',
			'Night_Shift_Wednesday',
			'Night_Shift_Thursday',
			'Night_Shift_Friday',
			'Night_Shift_Saturday',
			'Night_Shift_Sunday',
			'Beam_Monday',
			'Beam_Tuesday',
			'Beam_Wednesday',
			'Beam_Thursday',
			'Beam_Friday',
			'Beam_Saturday',
			'Beam_Sunday',
			'Source_Monday',
			'Source_Tuesday',
			'Source_Wednesday',
			'Source_Thursday',
			'Source_Friday',
			'Source_Saterday',
			'Source_Sunday',
			'Customer',
			'Prjoect_Code',
			'Scheduled_Hours',
			'Delivered_Hours',
			'No_Operators',
			'Notes_Monday',
			'Notes_Tuesday',
			'Notes_Wednesday',
			'Notes_Thursday',
			'Notes_Friday',
			'Notes_Saturday',	
		]

	