# Generated by Django 2.2.2 on 2019-11-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0118_auto_20191124_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='methodologies_processing_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
