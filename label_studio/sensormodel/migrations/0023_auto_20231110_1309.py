# Generated by Django 3.1.14 on 2023-11-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensormodel', '0022_auto_20231109_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='parsable_sensor_id',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]
