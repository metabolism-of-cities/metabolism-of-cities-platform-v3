# Generated by Django 2.1.3 on 2018-11-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplicity', '0007_datasettype_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasettypestructure',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]