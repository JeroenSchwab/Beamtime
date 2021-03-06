# Generated by Django 3.2.3 on 2021-10-19 09:16

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0033_auto_20210621_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Different_Beams',
        ),
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Energy',
        ),
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Flux',
        ),
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Hours',
        ),
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Ion_Species',
        ),
        migrations.CreateModel(
            name='BeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hours', models.IntegerField(default='1')),
                ('Flux', models.CharField(blank=True, max_length=50, null=True)),
                ('Energy', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Ion_Species', chained_model_field='Ion_Species', on_delete=django.db.models.deletion.CASCADE, to='beamrequest.energys')),
                ('Ion_Species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beamrequest.ionspecies')),
            ],
        ),
        migrations.AddField(
            model_name='createbeamrequestmodel',
            name='Beam_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.beammodel'),
        ),
    ]
