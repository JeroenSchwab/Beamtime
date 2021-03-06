# Generated by Django 3.2.3 on 2021-06-07 14:14

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0030_alter_createbeamrequestmodel_flux'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Energy',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Ion_Species', chained_model_field='Ion_Species', on_delete=django.db.models.deletion.CASCADE, to='beamrequest.energys'),
        ),
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Flux',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Ion_Species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beamrequest.ionspecies'),
        ),
    ]
