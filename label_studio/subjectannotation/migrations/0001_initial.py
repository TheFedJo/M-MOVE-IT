# Generated by Django 3.1.14 on 2023-10-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0016_auto_20220211_2218'),
        ('sensormodel', '0019_auto_20230927_1322'),
        ('data_import', '0002_auto_20231005_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectPresence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.FloatField(blank=True, null=True)),
                ('end_time', models.FloatField(blank=True, null=True)),
                ('file_upload', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data_import.fileupload')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sensormodel.subject')),
            ],
        ),
    ]
