# Generated by Django 3.2.3 on 2021-06-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Day_Shift_Sunday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Evening_Shift_Sunday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Night_Shift_Sunday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hourregistrationmodel',
            name='Day_Shift_Monday',
            field=models.CharField(blank=True, default='None', max_length=50, null=True),
        ),
    ]
