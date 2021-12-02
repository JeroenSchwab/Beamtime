from django import forms
from django.forms import TextInput

# validation errors for dates
from django.core.exceptions import ValidationError

#import the date/time picker
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

#import my models
from .models import CreateBeamRequestModel, IonSpecies, Energys #, BeamModel

#creating a form
class CreateBeamRequestForm(forms.ModelForm):

	# create meta class
	class Meta:

		# specify model to be used
		model = CreateBeamRequestModel

		# specify fields to be used
		fields = [
			'project_code',
			'pac_rate',
			'partrec_contact_name',
			'partrec_contact_email',
			'previous_experiment',
			'status',
			'project_title',
			'spokesperson_name',
			'spokesperson_adress',
			'spokesperson_phonenumber',
			'spokesperson_email',
			'collaborator_name',
			'collaborator_nationality',
			'collaborator_home_institute',
#			'Different_Beams',
#			'Shifts',
			'beam_note',
			'hours_requested',
			'ion_species',
			'energy',
			'flux',
			'start_date',
			'end_date',
			'requiered_equipment',
			'special_requirements',
			'special_safety_procedures',
			'lab_support_requirements',
			'funded',
			'summary',
#			'year',
#			'month',
#			'week',
#			'day',
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
			'project_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Project code'}),
			'partrec_contact_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of contact at Partrec'}),
			'partrec_contact_email':forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail of contact at Partrec'}),
			'previous_experiment':forms.TextInput(attrs={'class':'form-control','placeholder':'The name of the previous experiment if any'}),
			'project_title':forms.TextInput(attrs={'class':'form-control','placeholder':'The name of the project/experiment'}),
			'spokesperson_name':forms.TextInput(attrs={'class':'form-control','placeholder':'The name of the Spokesperson'}),
			'spokesperson_adress':forms.TextInput(attrs={'class':'form-control','placeholder':'The adress of the Spokesperson'}),
			'spokesperson_phonenumber':forms.TextInput(attrs={'class':'form-control','placeholder':'The phonenumber of the Spokesperson'}),
			'spokesperson_email':forms.TextInput(attrs={'class':'form-control','placeholder':'The e-mail adress of the Spokesperson'}),
			'collaborator_name':forms.TextInput(attrs={'class':'form-control','placeholder':'The name(s) of the collaborator(s)'}),
			'collaborator_nationality':forms.TextInput(attrs={'class':'form-control','placeholder':'The nationality of the collaborator(s)'}),
			'collaborator_home_institute':forms.TextInput(attrs={'class':'form-control','placeholder':'The institute of the collaborator(s)'}),
			'beam_note':forms.TextInput(attrs={'class':'form-control','placeholder':'Which beams if there are several?'}),
			'flux':forms.TextInput(attrs={'class':'form-control','placeholder':'The flux needed'}),
			'requiered_equipment':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Is there any extra equipment requiered for the experiment?'}),
			'special_requirements':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Are there any special requierements needed?'}),
			'special_safety_procedures':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Are there any special safety procedures that we should know?'}),
			'lab_support_requirements':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Is there any lab support requiered?'}),
			'funded':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'How is this experiment funded?'}),
			'summary':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'What are the steps in this experiment?'}),
#			'hours_requested':forms.Textarea(attrs={'class':'form-control','placeholder':'requested'}),

			'start_date': DateTimePickerInput(
				options = {
		          "format": "YYYY-MM-DD HH:mm", #date-time format
		          "showClose": True,
		          "showClear": True,
		          "showTodayButton": True,
		          "sideBySide": True,
        }
        ),

			'end_date': DateTimePickerInput(
				options = {
					"format": "YYYY-MM-DD HH:mm", #date-time format
					"showClose": True,
					"showClear": True,
					"showTodayButton": True,
					"sideBySide": True,
			}
			),
		}


# Logic for raising error if end_date < start_date
	def clean(self): #*args, **kwargs):
		cleaned_data = super().clean()
#		print(dir(self))
#		print(cleaned_data)
		start_date = cleaned_data.get("start_date")
		end_date = cleaned_data.get("end_date")
#		print(start_date)
#		print(end_date)
		if end_date < start_date:
			#raise forms.ValidationError({"End_Date": "End date should be greater than start date."})
			raise forms.ValidationError("End date should be later than start date.")
		return cleaned_data