# Generated by Django 3.2 on 2021-05-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0008_auto_20210512_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Ion_Species',
            field=models.CharField(choices=[('Select', 'Select Ion species'), ('P', 'Protons'), ('4He', 'Helium'), ('12C', 'Carbon')], default='SELECT', max_length=20),
        ),
    ]
