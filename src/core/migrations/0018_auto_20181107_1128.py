# Generated by Django 2.1.2 on 2018-11-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20181103_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='hidden',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
