# Generated by Django 2.1.3 on 2019-01-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20181211_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('research', 'Thesis project'), ('regular', 'Research project'), ('applied', 'Applied project')], max_length=20),
        ),
    ]