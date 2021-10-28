# Generated by Django 3.2.3 on 2021-07-17 19:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hours.models


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0033_auto_20210621_2218'),
        ('hours', '0018_auto_20210710_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friday',
            name='Day_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Friday_Day_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='friday',
            name='Evening_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Friday_Evening_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='friday',
            name='Night_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Friday_Night_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='hourregistrationmodel',
            name='Week',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52)], default=28),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='Day_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Saturday_Day_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='Evening_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Saturday_Evening_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='Night_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Saturday_Night_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='Day_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sunday_Day_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='Evening_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sunday_Evening_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='Night_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sunday_Night_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='Day_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thursday_Day_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='Evening_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thursday_Evening_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='Night_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tursday_Night_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='tuesday',
            name='Evening_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tuesday_Evening_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='tuesday',
            name='Night_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tuesday_Night_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='Day_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Wednesday_Day_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='Evening_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Wednesday_Evening_Shift', to='hours.operators'),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='Night_Shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Wednesday_Night_Shift', to='hours.operators'),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(2020), hours.models.max_value_current_year])),
                ('Week', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52)], default=28)),
                ('Customer', models.CharField(blank=True, max_length=50, null=True)),
                ('Scheduled_Hours', models.CharField(blank=True, max_length=50, null=True)),
                ('Delivered_Hours', models.CharField(blank=True, max_length=50, null=True)),
                ('No_Operators', models.CharField(blank=True, max_length=50, null=True)),
                ('Notes', models.TextField(blank=True, null=True)),
                ('Beam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.ionspecies')),
                ('Day_Shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Day_Shift', to='hours.operators')),
                ('Evening_Shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Evening_Shift', to='hours.operators')),
                ('Night_Shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Night_Shift', to='hours.operators')),
                ('Project_Code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.createbeamrequestmodel')),
                ('Source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hours.source')),
            ],
        ),
    ]