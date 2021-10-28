from django import forms
from django.forms import TextInput

# validation errors for dates
from django.core.exceptions import ValidationError

#import the date/time picker
#from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

#import my models
from .models import HourRegistrationModel

		
#creating a form
class HourRegistrationForm(forms.ModelForm):

	hours_requested = forms.CharField(widget=forms.TextInput, label='')

	# create meta class
	class Meta:

		# specify model to be used
		model = HourRegistrationModel

		# specify fields to be used
		fields = [
			'year',
			'month',
			'week',
			'day',
			'project_code',
			'hours_requested',
			'hours_deliverd',
			'woak',
			'planned',
			'unused',
			'defelopment',
			'calibration',
			'general_error',
			'rf_error',
			'emc1_error',
			'foeldi_error',
			'cryo_error',
			'other_error',
			'notes',

		]
		widgets = {
			'hours_requested':forms.Textarea(attrs={'class':'form-control','placeholder':'requested'}),
		}