# Generated by Django 3.2.3 on 2021-06-03 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0023_auto_20210601_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Ion_Species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.ionspecies'),
        ),
    ]