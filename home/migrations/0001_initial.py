# Generated by Django 4.1.5 on 2023-02-01 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadManagement',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('mobile_number', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100)),
                ('address', models.TextField()),
                ('industry', models.CharField(max_length=125)),
                ('website', models.URLField()),
                ('contacts', models.CharField(max_length=126)),
                ('pipelines', models.TextField()),
                ('notes', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
