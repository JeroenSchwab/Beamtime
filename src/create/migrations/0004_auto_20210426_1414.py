# Generated by Django 3.2 on 2021-04-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0003_rename_reqdata_reqdatamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqdatamodel',
            name='PacRate',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reqdatamodel',
            name='PartrecContactEmail',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reqdatamodel',
            name='PartrecContactName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reqdatamodel',
            name='ProjectCode',
            field=models.CharField(max_length=20),
        ),
    ]
