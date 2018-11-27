# Generated by Django 2.1.3 on 2018-11-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplicity', '0017_information_processes'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphtype',
            name='timeframes',
            field=models.CharField(choices=[('single', 'Single material'), ('multiple', 'Multiple materials'), ('both', 'Does not matter')], default='both', max_length=25),
        ),
    ]