# Generated by Django 3.2.3 on 2021-11-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0030_auto_20211102_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourregistrationmodel',
            name='day',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], default=5),
        ),
    ]
