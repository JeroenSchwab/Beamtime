# Generated by Django 3.2.3 on 2021-07-10 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0015_alter_monday_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
        migrations.RenameField(
            model_name='monday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
        migrations.RenameField(
            model_name='saturday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
        migrations.RenameField(
            model_name='sunday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
        migrations.RenameField(
            model_name='thursday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
        migrations.RenameField(
            model_name='tuesday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
        migrations.RenameField(
            model_name='wednesday',
            old_name='Prjoect_Code',
            new_name='Project_Code',
        ),
    ]
