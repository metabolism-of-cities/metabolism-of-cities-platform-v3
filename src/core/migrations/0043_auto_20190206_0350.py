# Generated by Django 2.1.3 on 2019-02-06 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20190205_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thesistype',
            field=models.CharField(blank=True, choices=[('bachelor', 'Bachelor'), ('masters', 'Master'), ('phd', 'PhD')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='website',
            field=models.CharField(choices=[('youtube', 'YouTube'), ('vimeo', 'Vimeo'), ('wikimedia', 'Wikimedia Commons'), ('other', 'Other website')], max_length=20),
        ),
    ]
