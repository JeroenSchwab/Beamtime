from django import forms
from django.forms import TextInput

# validation errors for dates
from django.core.exceptions import ValidationError

#import the date/time picker
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

#import my models
from .models import CreateBeamRequestModel, IonSpecies, Energys

#creating a form
class CreateBeamRequestForm(forms.ModelForm):

	# create meta class
	class Meta:

		# specify model to be used
		model = CreateBeamRequestModel

		# specify fields to be used
		fields = [
			'Project_Code',
			'Pac_Rate',
			'Partrec_Contact_Name',
			'Partrec_Contact_Email',
			'Previous_Experiment',
			'Status',
			'Project_Title',
			'Spokesperson_Name',
			'Spokesperson_Adress',
			'Spokesperson_Phonenumber',
			'Spokesperson_Email',
			'Collaborator_Name',
			'Collaborator_Nationality',
			'Collaborator_Home_Institute',
			'Different_Beams',
#			'Shifts',
			'Hours',
			'Ion_Species',
			'Energy',
			'Flux',
			'Start_Date',
			'End_Date',
			'Requiered_Equipment',
			'Special_Requirements',
			'Special_Safety_Procedures',
			'Lab_Support_Requirements',
			'Funded',
			'Summary',
		]
		widgets = {
			'Project_Code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Project code'}),
			'Partrec_Contact_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of contact at Partrec'}),
			'Partrec_Contact_Email':forms.TextInput(attrs={'class':'form-control','placeholder':'E-mail of contact at Partrec'}),
			'Previous_Experiment':forms.TextInput(attrs={'class':'form-control','placeholder':'The name of the previous experiment if any'}),
			'Project_Title':forms.TextInput(attrs={'class':'form-control','placeholder':'The name of the project/experiment'}),
			'Spokesperson_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'The name of the Spokesperson'}),
			'Spokesperson_Adress':forms.TextInput(attrs={'class':'form-control','placeholder':'The adress of the Spokesperson'}),
			'Spokesperson_Phonenumber':forms.TextInput(attrs={'class':'form-control','placeholder':'The phonenumber of the Spokesperson'}),
			'Spokesperson_Email':forms.TextInput(attrs={'class':'form-control','placeholder':'The e-mail adress of the Spokesperson'}),
			'Collaborator_Name':forms.TextInput(attrs={'class':'form-control','placeholder':'The name(s) of the collaborator(s)'}),
			'Collaborator_Nationality':forms.TextInput(attrs={'class':'form-control','placeholder':'The nationality of the collaborator(s)'}),
			'Collaborator_Home_Institute':forms.TextInput(attrs={'class':'form-control','placeholder':'The institute of the collaborator(s)'}),
			'Flux':forms.TextInput(attrs={'class':'form-control','placeholder':'The flux needed'}),
			'Requiered_Equipment':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Is there any extra equipment requiered for the experiment?'}),
			'Special_Requirements':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Are there any special requierements needed?'}),
			'Special_Safety_Procedures':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Are there any special safety procedures that we should know?'}),
			'Lab_Support_Requirements':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Is there any lab support requiered?'}),
			'Funded':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'How is this experiment funded?'}),
			'Summary':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'What are the steps in this experiment?'}),

			'Start_Date': DateTimePickerInput(
				options = {
          "format": "YYYY-MM-DD HH:mm", #date-time format
          "showClose": True,
          "showClear": True,
          "showTodayButton": True,
          "sideBySide": True,
        }
        ),

			'End_Date': DateTimePickerInput(
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
		start_date = cleaned_data.get("Start_Date")
		end_date = cleaned_data.get("End_Date")
#		print(start_date)
#		print(end_date)
		if end_date < start_date:
			#raise forms.ValidationError({"End_Date": "End date should be greater than start date."})
			raise forms.ValidationError("End date should be later than start date.")
		return cleaned_data