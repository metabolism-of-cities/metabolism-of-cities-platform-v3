# Generated by Django 2.1.3 on 2019-02-05 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20190205_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='website',
            field=models.CharField(choices=[('youtube', 'YouTube'), ('vimeo', 'Vimeo')], max_length=20),
        ),
    ]
