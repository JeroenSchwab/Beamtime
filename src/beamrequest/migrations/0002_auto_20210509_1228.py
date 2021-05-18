# Generated by Django 3.2 on 2021-05-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBeamRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Code', models.CharField(blank=True, max_length=20)),
                ('Pac_Rate', models.CharField(blank=True, max_length=10)),
                ('Partrec_Contact_Name', models.CharField(blank=True, max_length=50)),
                ('Partrec_Contact_Email', models.EmailField(blank=True, max_length=254)),
                ('Previous_Experiment', models.CharField(blank=True, max_length=200)),
                ('Project_Title', models.CharField(blank=True, max_length=100)),
                ('Spokesperson_Name', models.CharField(blank=True, max_length=50)),
                ('Spokesperson_Adress', models.CharField(blank=True, max_length=50)),
                ('Spokesperson_Phonenumber', models.CharField(blank=True, max_length=20)),
                ('Spokesperson_Email', models.EmailField(blank=True, max_length=254)),
                ('Collaborator_Name', models.TextField(blank=True)),
                ('Collaborator_Nationality', models.TextField(blank=True)),
                ('Collaborator_Home_Institute', models.TextField(blank=True)),
                ('Shifts', models.CharField(blank=True, max_length=20)),
                ('Ion_Spiecies', models.CharField(blank=True, max_length=20)),
                ('Energy', models.CharField(blank=True, max_length=20)),
                ('Flux', models.CharField(blank=True, max_length=20)),
                ('Start_Date', models.DateTimeField()),
                ('End_Date', models.DateTimeField(blank=True, max_length=20)),
                ('Requiered_Equipment', models.TextField(blank=True)),
                ('Special_Requirements', models.TextField(blank=True)),
                ('Special_Safty_Pocedures', models.TextField(blank=True)),
                ('Lab_Support_Requirements', models.TextField(blank=True)),
                ('Funded', models.CharField(blank=True, max_length=20)),
                ('Summery', models.TextField(blank=True)),
                ('Status', models.CharField(choices=[('Select', 'Select an option'), ('Request', 'Request'), ('Tentavive', 'Tentative'), ('Accepted', 'Accepted'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Queued', 'Queued')], default='SELECT', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CreateBeamRequest',
        ),
    ]
