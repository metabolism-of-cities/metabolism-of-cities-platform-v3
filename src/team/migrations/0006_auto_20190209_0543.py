# Generated by Django 2.1.3 on 2019-02-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20190209_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='show_publicly',
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]