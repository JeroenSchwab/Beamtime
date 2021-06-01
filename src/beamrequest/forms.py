from django import forms
from django.forms import TextInput

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
			'Shifts',
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
			'Requiered_Equipment':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Is there any extra equipment requiered for the experiment?'}),
			'Special_Requirements':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Are there any special requierements needed?'}),
			'Special_Safety_Procedures':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Are there any special safety procedures that we should know?'}),
			'Lab_Support_Requirements':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'Is there any lab support requiered?'}),
			'Funded':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'How is this experiment funded?'}),
			'Summary':forms.Textarea(attrs={'rows':5, 'cols':500, 'class':'form-control','placeholder':'What are the steps in this experiment?'}),

			'Start_Date': DateTimePickerInput(
			options = {
                       "format": "DD/MM/YYYY HH:mm", # moment date-time format
                       "showClose": True,
                       "showClear": True,
                       "showTodayButton": True,
#                      "sideBySide": True,
                      }
            ),

			'End_Date': DateTimePickerInput(
			options = {
						"format": "DD/MM/YYYY HH:mm", # moment date-time format
						"showClose": True,
						"showClear": True,
						"showTodayButton": True,
#						"sideBySide": True,
			}
			),
		}

	#def __init__(self, *args, **kwargs):
	#	super().__init__(*args, **kwargs)
	#	self.fields['Energy'].queryset = Energys.objects.none()

	#	if 'id_Ion_Species' in self.data:
	#		try:
	#			ionspeciesid = int(self.data.get('id_Ion_Species'))
	#			self.fields['Energy'].queryset = Energy.objects.filter(Ion_Species_id=ionspeciesid).order_by('energy')
	#		except (ValueError, TypeError):
	#			pass  # invalid input from the client; ignore and fallback to empty City queryset
	#	elif self.instance.pk:
	#		self.fields['Energy'].queryset = self.instance.Ion_Species.Energy_set.order_by('energy')
