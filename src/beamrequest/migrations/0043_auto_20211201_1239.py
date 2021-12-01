# Generated by Django 3.2.3 on 2021-12-01 11:39

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0042_auto_20211201_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Beam_Note',
            new_name='beam_note',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Collaborator_Home_Institute',
            new_name='collaborator_home_institute',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Collaborator_Name',
            new_name='collaborator_name',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Collaborator_Nationality',
            new_name='collaborator_nationality',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='End_Date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Flux',
            new_name='flux',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Funded',
            new_name='funded',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Hours',
            new_name='hours_requested',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Ion_Species',
            new_name='ion_species',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Lab_Support_Requirements',
            new_name='lab_support_requirements',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Pac_Rate',
            new_name='pac_rate',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Partrec_Contact_Email',
            new_name='partrec_contact_email',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Partrec_Contact_Name',
            new_name='partrec_contact_name',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Previous_Experiment',
            new_name='previous_experiment',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Project_Code',
            new_name='project_code',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Project_Title',
            new_name='project_title',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Requiered_Equipment',
            new_name='requiered_equipment',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Special_Requirements',
            new_name='special_requirements',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Special_Safety_Procedures',
            new_name='special_safety_procedures',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Spokesperson_Adress',
            new_name='spokesperson_adress',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Spokesperson_Email',
            new_name='spokesperson_email',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Spokesperson_Name',
            new_name='spokesperson_name',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Spokesperson_Phonenumber',
            new_name='spokesperson_phonenumber',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Start_Date',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='createbeamrequestmodel',
            old_name='Summary',
            new_name='summary',
        ),
        migrations.RenameField(
            model_name='energys',
            old_name='Ion_Species',
            new_name='ion_species',
        ),
        migrations.RenameField(
            model_name='energys',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ionspecies',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Energy',
        ),
        migrations.AddField(
            model_name='createbeamrequestmodel',
            name='energy',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='ion_species', chained_model_field='ion_species', null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.energys'),
        ),
    ]