from django.db import models

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

    #different beam choices (1 to 10)
	DIFBEAMS_CHOICES = [tuple([x,x]) for x in range(1,11)]

	#shift choices (1 to 16)
	SHIFTS_CHOICES = [tuple([x,x]) for x in range(1,17)]

	#Ion_Species choices
	SELECT = 'Select'
	HYDROGEN = 'H'
	HELIUM = 'He'
	LITHIUM = 'Li'
	BORON = 'B'
	CARBON = 'C'
	NITROGEN = 'N'
	OXYGEN = 'O'
	FLUORINE = 'F'
	NEON = 'Ne'
	SODIUM = 'Na'
	MAGNESIUM = 'Mg'
	ARGON = 'Ar'
	CALCIUM = 'Ca'
	KRYPTON= 'Kr'
	XENON = 'Xe'
	LEAD = 'Pb'

	ION_CHOICES = [
		(SELECT, ('Select Ion species')),
		(HYDROGEN, ('H or P')),
		(HELIUM, ('He')),
		(LITHIUM, ('Li')),
		(BORON, ('B')),
		(CARBON, ('C')),
		(NITROGEN, ('N')),
		(OXYGEN, ('O')),
		(FLUORINE, ('F')),
 		(NEON, ('Ne')),
		(SODIUM, ('Na')),
		(MAGNESIUM, ('Mg')),
		(ARGON, ('Ar')),
		(CALCIUM, ('Ca')),
		(KRYPTON, ('Kr')),
		(XENON, ('Xe')),
		(LEAD, ('Pb')),
	]

	ION_ENERGY_CHOICES = [ 
	('H', (('THIRTYFOUR', '34 MeV'), ('FORTY', '40 MeV'), ('FORTYTHREE', '43 MeV'),	('FORTYFIVE', '45 MeV'), ('FIFTY', '50 MeV'), ('FIFTYFIVE', '55 MeV'), ('SIXTY', '60 MeV'), ('SIXTYSIXHALVE', '66.5 MeV'), ('EIGHTY', '80 MeV'), ('EIGHTYFIVE', '85 MeV'), ('NINETY', '90 MeV'),('HUNDREDTWNTY', '120 MeV'),('HUNDREDTHIRTYFIVE', '135 MeV'), ('HUNDREDFIFTY', '150 MeV'), ('HUNDREDSEVENTY', '170 MeV'), ('HUNDREDEIGHTY', '180 MeV'), ('HUNDREDNINETY', '190 MeV'), )),
	('He', (('FOURTEENTHIRTYTHREE', '14.33 MeV'), ('EIGHTEEN', '18 MeV'), ('THIRTY', '30 MeV'), ('THIRTYFOUR', '34 MeV'), ('FORTY', '40 MeV'), ('FORTYTHREE', '43 MeV'), ('FORTYFIVE', '45 MeV'), ('FIFTY', '50 MeV'), ('FIFTYFIVE', '55 MeV'), ('FIFTYNINE', '59 MeV'), ('SIXTY', '60 MeV'), ('SIXTYSIXHALVE', '66.5 MeV'), ('EIGHTY', '80 MeV'), ('EIGHTYTHREE', '83 MeV'), ('EIGHTYFIVE', '85 MeV'), ('EIGHTYSEVEN', '87 MeV'), ('NINETY', '90 MeV'), )),
	('Li', (('EIGHT', '8 MeV'),	('THIRTEENEIGHT', '13.8 MeV'), )),
	('B', (('EIGHTEENHALVE', '18.5 MeV'), )),
	('C', (('EIGHT', '8 MeV'), ('FOURTEENTHIRTYTHREE', '14.33 MeV'), ('EIGHTEEN', '18 MeV'), ('TWNETYFIVE', '25 MeV'), ('TWENTYTWOSEVEN', '22.7 MeV'), ('THIRTY', '30 MeV'), ('THIRTYFOUR', '34 MeV'), ('FORTY', '40 MeV'), ('FORTYTHREE', '43 MeV'), ('FORTYFIVE', '45 MeV'), ('FIFTY', '50 MeV'), ('FIFTYFIVE', '55 MeV'), ('SIXTY', '60 MeV'), ('SIXTYSIXHALVE', '66.5 MeV'), ('EIGHTY', '80 MeV'), ('EIGHTYFIVE', '85 MeV'), ('NINETY', '90 MeV'), )),
	('N', (('SEVEN', '7 MeV'), ('TEN', '10 MeV'), ('TWELVE', '12 MeV'), )),
	('O', (('EIGHT', '8 MeV'), ('FOURTEENTHIRTYTHREE', '14.33 MeV'), ('EIGHTEEN', '18 MeV'), ('THIRTY', '30 MeV'), ('THIRTYFOUR', '34 MeV'), ('FORTY', '40 MeV'), ('FORTYTHREE', '43 MeV'), ('FORTYFIVE', '45 MeV'), ('FIFTY', '50 MeV'), ('FIFTYFIVE', '55 MeV'), ('SIXTY', '60 MeV'), ('SIXTYSIXHALVE', '66.5 MeV'), ('EIGHTY', '80 MeV'), ('EIGHTYFIVE', '85 MeV'), ('NINETY', '90 MeV'), )),
	('F', (('TEN', '10 MeV'), ('TENHALVE', '10.5 MeV'), ('FORTYTHREE', '43 MeV'), )),
	('Ne', (('TEN', '10 MeV'), ('TWENTY', '20 MeV'), ('TWENTYTHREE', '23 MeV'), ('TWENTYTHREETHREE', '23.3 MeV'), ('THIRTY', '30 MeV'), ('THIRTYFOUR', '34 MeV'), ('FORTY', '40 MeV'), ('FORTYTHREE', '43 MeV'), ('FORTYFIVE', '45 MeV'), ('FIFTY', '50 MeV'), ('FIFTYFIVE', '55 MeV'), ('SIXTY', '60 MeV'), ('SIXTYSIXHALVE', '66.5 MeV'), ('EIGHTY', '80 MeV'), ('EIGHTYFIVE', '85 MeV'), ('NINETY', '90 MeV'), )),
	('Na', (('THIRTYTWO', '32 MeV'), )),
	('Mg', (('THIRTY', '30 MeV'), ('FIFTYFIVE', '55 MeV'), )),
	('Ar', (('EIGHT', '8 MeV'), ('THIRTY', '30 MeV'), ('SIXTY', '60 MeV'),)),
	('Ca', (('FORTYFIVE', '45 MeV'), )),
	('Kr', (('TWNETYFIVE', '25 MeV'), )),
	('Xe', (('EIGHT', '8 MeV'), )),
	('Pb', (('EIGHT', '8 MeV'), ('EIGHTHALVE', '8.5 MeV'), ('NINEHALVE', '9.5 MeV'), ('ELEVENTHREE', '11.3 MeV'), )),
    ]
	



	#Energy choices
	SELECT = 'Select'
	SEVEN = '7 MeV'
	EIGHT = '8 MeV'
	EIGHTHALVE = '8.5 MeV'
	NINEHALVE = '9.5 MeV'
	TEN = '10 MeV'
	TENHALVE = '10.5 MeV'
	ELEVENTHREE = '11.3 MeV'
	TWELVE = '12 MeV'
	THIRTEENEIGHT = '13.8 MeV'
	FOURTEENTHIRTYTHREE = '14.33 MeV'
	EIGHTEEN = '18 MeV'
	EIGHTEENHALVE = '18.5 MeV'
	TWENTY = '20 MeV'
	TWENTYTWOSEVEN = '22.7 MeV'
	TWENTYTHREE = '23 MeV'
	TWENTYTHREETHREE = '23.3 MeV'
	TWNETYFIVE = '25 MeV'
	THIRTY = '30 MeV'
	THIRTYTWO = '32 MeV'
	THIRTYFOUR = '34 MeV'
	FORTY = '40 MeV'
	FORTYTHREE = '43 MeV'
	FORTYFIVE = '45 MeV'
	FIFTY = '50 MeV'
	FIFTYFIVE = '55 MeV'
	FIFTYNINE = '59 MeV'
	SIXTY = '60 MeV'
	SIXTYSIXHALVE = '66.5 MeV'
	EIGHTY = '80 MeV'
	EIGHTYTHREE = '83 MeV'
	EIGHTYFIVE = '85 MeV'
	EIGHTYSEVEN = '87 MeV'
	NINETY = '90 MeV'
	HUNDREDTWNTY = '120 MeV'
	HUNDREDTHIRTYFIVE = '135 MeV'
	HUNDREDFIFTY = '150 MeV'
	HUNDREDSIXTY = '160 MeV'
	HUNDREDSEVENTY = '170 MeV'
	HUNDREDEIGHTY = '180 MeV'
	HUNDREDNINETY = '190 MeV'

	ENERGY_CHOICES = [
		(SELECT, ('Select Energy')),
		(NINETY, ('90MeV')),
		(HUNDREDFIFTY, ('150 MeV')),
		(HUNDREDNINETY, ('190 MeV')),
	]

	#fields of the model
	Project_Code = models.CharField(max_length=20, blank = True)
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
	Ion_Species = models.CharField(max_length=20, choices=ION_CHOICES, default='H')
	Energy = models.CharField(max_length=20, choices=ION_ENERGY_CHOICES, default='SELECT')
	Flux = models.CharField(max_length=20, blank = True)
	Start_Date = models.DateTimeField(blank = True)
	End_Date = models.DateTimeField(blank = True)
	Requiered_Equipment = models.TextField(blank = True)
	Special_Requirements = models.TextField(blank = True)
	Special_Safety_Procedures = models.TextField(blank = True)
	Lab_Support_Requirements = models.TextField(blank = True)
	Funded = models.CharField(max_length=20, blank = True)
	Summary = models.TextField(blank = True)

