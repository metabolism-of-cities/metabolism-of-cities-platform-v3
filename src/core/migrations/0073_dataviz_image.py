# Generated by Django 2.2.2 on 2019-08-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_dataviz'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataviz',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dataviz'),
        ),
    ]
