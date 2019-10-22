# Generated by Django 2.2.2 on 2019-10-22 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_method_methodscale'),
    ]

    operations = [
        migrations.AddField(
            model_name='method',
            name='material_scope',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='method',
            name='between_flows',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], help_text='Specification of flows between sectors, industries or acticity fields, or other system components', max_length=1, null=True, verbose_name='between-flows'),
        ),
        migrations.AlterField(
            model_name='method',
            name='energy',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='method',
            name='entity',
            field=models.CharField(blank=True, help_text='Key socio-institutional entity (driving force boundary for induced flows)', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='method',
            name='materials',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True, verbose_name='materials / bulk materials'),
        ),
        migrations.AlterField(
            model_name='method',
            name='outputs',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True, verbose_name='outputs to environment'),
        ),
        migrations.AlterField(
            model_name='method',
            name='production',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True, verbose_name='production processes'),
        ),
        migrations.AlterField(
            model_name='method',
            name='recycling',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True, verbose_name='recyling of material and energy'),
        ),
        migrations.AlterField(
            model_name='method',
            name='specific',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True, verbose_name='specific goods and services'),
        ),
        migrations.AlterField(
            model_name='method',
            name='stock_changes',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], max_length=1, null=True, verbose_name='stock changes'),
        ),
        migrations.AlterField(
            model_name='method',
            name='substances',
            field=models.CharField(blank=True, choices=[(3, '3 - The item is a defining feature of the approach'), (2, '2 - The feature is typically included in the techique'), (1, '1 - The item is included only occasionally in the mode of analysis, and in a partial or conditional way')], help_text='Elements and basic compounds only', max_length=1, null=True, verbose_name='selected specific substances'),
        ),
        migrations.AlterField(
            model_name='method',
            name='tag',
            field=models.OneToOneField(limit_choices_to={'parent_tag__id': 318}, on_delete=django.db.models.deletion.CASCADE, to='core.Tag'),
        ),
    ]
