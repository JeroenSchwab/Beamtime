# Generated by Django 3.2.3 on 2021-06-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0031_auto_20210607_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Funded',
            field=models.TextField(blank=True),
        ),
    ]