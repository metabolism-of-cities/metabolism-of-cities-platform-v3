# Generated by Django 2.1.3 on 2018-11-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staf', '0004_auto_20181103_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='symbol',
            field=models.CharField(max_length=255),
        ),
    ]