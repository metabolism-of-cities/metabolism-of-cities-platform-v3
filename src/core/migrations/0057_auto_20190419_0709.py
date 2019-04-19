# Generated by Django 2.1.3 on 2019-04-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplicity', '0048_photo_position'),
        ('core', '0056_auto_20190419_0657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='primary_space',
        ),
        migrations.AddField(
            model_name='reference',
            name='spaces',
            field=models.ManyToManyField(blank=True, to='multiplicity.ReferenceSpace'),
        ),
    ]