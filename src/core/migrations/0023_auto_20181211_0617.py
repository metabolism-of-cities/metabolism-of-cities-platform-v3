# Generated by Django 2.1.3 on 2018-12-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_reference_processes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]