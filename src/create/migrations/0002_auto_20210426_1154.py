# Generated by Django 3.2 on 2021-04-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reqdata',
            name='PacRate',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reqdata',
            name='PartrecContactEmail',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reqdata',
            name='PartrecContactName',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reqdata',
            name='ProjectCode',
            field=models.TextField(blank=True),
        ),
    ]
