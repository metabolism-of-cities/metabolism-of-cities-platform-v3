# Generated by Django 2.1.3 on 2019-04-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staf', '0013_csv_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialcatalog',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='materialcatalog',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
