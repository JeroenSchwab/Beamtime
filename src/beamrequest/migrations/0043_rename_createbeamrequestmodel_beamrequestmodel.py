# Generated by Django 3.2.3 on 2021-12-06 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0036_auto_20211206_1606'),
        ('documentation', '0004_alter_add_file_model_file'),
        ('beamrequest', '0042_alter_createbeamrequestmodel_energy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateBeamRequestModel',
            new_name='BeamRequestModel',
        ),
    ]
