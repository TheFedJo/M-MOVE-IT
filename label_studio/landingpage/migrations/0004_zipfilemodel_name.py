# Generated by Django 3.1.14 on 2024-02-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_zipfilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='zipfilemodel',
            name='name',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
