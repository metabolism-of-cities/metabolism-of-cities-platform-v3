# Generated by Django 2.1.2 on 2018-10-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20181030_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='people',
            field=models.ManyToManyField(blank=True, to='core.People'),
        ),
    ]
