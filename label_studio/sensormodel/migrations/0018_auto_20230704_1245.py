# Generated by Django 3.2.16 on 2023-07-04 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensormodel', '0017_auto_20230525_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deployment',
            name='sensorlist',
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='subjectlist',
        ),
        migrations.AlterField(
            model_name='deployment',
            name='location',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='sensor',
        ),
        migrations.AddField(
            model_name='deployment',
            name='sensor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sensormodel.sensor'),
        ),
        migrations.RemoveField(
            model_name='deployment',
            name='subject',
        ),
        migrations.AddField(
            model_name='deployment',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sensormodel.subject'),
        ),
    ]
