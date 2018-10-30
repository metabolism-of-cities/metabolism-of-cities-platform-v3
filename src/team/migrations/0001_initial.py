# Generated by Django 2.1.2 on 2018-10-28 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('google_drive', models.CharField(blank=True, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('category_description', models.TextField(null=True)),
                ('slug', models.SlugField()),
                ('group', models.CharField(choices=[('community', 'Community'), ('services', 'Services'), ('project', 'Project'), ('board', 'Administrative board')], default='community', max_length=10)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('file', models.FileField(null=True, upload_to='uploads/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='MessageRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='team.Message')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('funders', models.CharField(blank=True, max_length=255, null=True)),
                ('partners', models.CharField(blank=True, max_length=255, null=True)),
                ('our_budget', models.CharField(blank=True, max_length=255, null=True)),
                ('total_budget', models.CharField(blank=True, max_length=255, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='description')),
                ('budget_breakdown', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Budget breakdown')),
                ('logos', models.ImageField(blank=True, null=True, upload_to='projectlogos')),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('public', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('deciding', 'Not yet internally approved'), ('no_go', 'Internal decision not to proceed'), ('drafing', 'Internally approved; proposal is being drafted'), ('submitted', 'Submitted; in review'), ('declined', 'Declined'), ('approved', 'Approved; not yet started'), ('work', 'Approved; in progress'), ('completed', 'Approved; project completed')], default='not_submitted', max_length=20)),
                ('taskforce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', tinymce.models.HTMLField(verbose_name='Description')),
                ('price_range', models.CharField(blank=True, max_length=255, null=True)),
                ('possible_partners', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Possible partners')),
                ('public', models.BooleanField(default=True)),
                ('available_members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskForceMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_subscription', models.CharField(choices=[('instantly', 'Instant notification'), ('daily', 'Daily digest'), ('weekly', 'Weekly digest'), ('none', 'No subscription')], default='instantly', max_length=10)),
                ('role', models.CharField(choices=[('leader', 'Leader'), ('member', 'Member'), ('reader', 'Reader')], default='member', max_length=10)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('notify_of_new_topics', models.BooleanField()),
                ('taskforce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskForceTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='description')),
                ('urgency', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=6)),
                ('importance', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=6)),
                ('complexity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('unassigned', 'Unassigned'), ('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('shelved', 'Shelved'), ('completed', 'Completed'), ('removed', 'Removed')], default='unassigned', max_length=20)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('taskforce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Category')),
            ],
        ),
        migrations.CreateModel(
            name='TaskForceUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('taskforce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Category')),
            ],
        ),
        migrations.CreateModel(
            name='TicketLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='description')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.TaskForceTicket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='topics', to='team.Category')),
                ('last_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_message', to='team.Message')),
            ],
        ),
        migrations.CreateModel(
            name='TopicSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('instantly', 'Instant notification'), ('daily', 'Daily digest'), ('weekly', 'Weekly digest')], default='instantly', max_length=10)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribed_to', through='team.TopicSubscription', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskforceticket',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Topic'),
        ),
        migrations.AddField(
            model_name='taskforceticket',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.TaskForceUnit'),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Service'),
        ),
        migrations.AddField(
            model_name='messageread',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='team.Topic'),
        ),
        migrations.AddField(
            model_name='messageread',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Topic'),
        ),
        migrations.AddField(
            model_name='category',
            name='members',
            field=models.ManyToManyField(through='team.TaskForceMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
