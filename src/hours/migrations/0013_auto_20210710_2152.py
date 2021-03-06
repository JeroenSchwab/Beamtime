# Generated by Django 3.2.3 on 2021-07-10 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0012_auto_20210710_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Friday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hours.friday'),
        ),
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Saturday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hours.saturday'),
        ),
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Sunday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hours.sunday'),
        ),
        migrations.AddField(
            model_name='hourregistrationmodel',
            name='Thursday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hours.thursday'),
        ),
    ]
