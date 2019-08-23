# Generated by Django 2.2.2 on 2019-08-23 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_auto_20190821_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='newslettersubscriber',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='people',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='video',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='videocollection',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
