# Generated by Django 2.1.3 on 2018-11-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20181125_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='title_original_language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
