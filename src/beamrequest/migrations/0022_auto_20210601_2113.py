# Generated by Django 3.2.3 on 2021-06-01 19:13

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0021_alter_createbeamrequestmodel_project_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='energys',
            old_name='energy',
            new_name='Energy',
        ),
        migrations.RenameField(
            model_name='ionspecies',
            old_name='ionspecie',
            new_name='Ion_Species',
        ),
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Energy',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Ion_Species', chained_model_field='Ion_Species', null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.energys'),
        ),
    ]
