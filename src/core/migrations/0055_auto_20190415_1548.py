# Generated by Django 2.1.3 on 2019-04-15 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20190305_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceAuthors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.People')),
            ],
            options={
                'db_table': 'core_reference_authors',
            },
        ),
        migrations.AlterField(
            model_name='reference',
            name='authors',
            field=models.ManyToManyField(through='core.ReferenceAuthors', to='core.People'),
        ),
        migrations.AddField(
            model_name='referenceauthors',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Reference'),
        ),
    ]