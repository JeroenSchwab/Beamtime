# Generated by Django 3.2.3 on 2021-12-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0037_remove_hourregistrationmodel_hours_deliverd'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='hours_deliverd',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
