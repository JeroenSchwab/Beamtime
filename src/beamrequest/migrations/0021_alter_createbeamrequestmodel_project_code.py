# Generated by Django 3.2.3 on 2021-06-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0020_auto_20210529_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbeamrequestmodel',
            name='Project_Code',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
