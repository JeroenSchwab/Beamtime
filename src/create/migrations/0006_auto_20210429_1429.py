# Generated by Django 3.2 on 2021-04-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0005_auto_20210428_2039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AlterField(
            model_name='reqdatamodel',
            name='PartrecContactEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='reqdatamodel',
            name='SpokesPersonEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
