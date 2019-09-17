# Generated by Django 2.2.2 on 2019-09-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_auto_20190828_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='file',
            field=models.FileField(blank=True, help_text='Only upload the file if you are the creator or you have permission to do so', null=True, upload_to='references'),
        ),
    ]
