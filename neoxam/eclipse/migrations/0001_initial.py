# Generated by Django 4.2 on 2023-05-03 16:02

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliverTestTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('schema_version', models.PositiveIntegerField()),
                ('procedure_name', models.CharField(max_length=255)),
                ('procedure_test_name', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('compiling', 'Compiling'), ('success', 'Success'), ('failed', 'Failed')], default='compiling', max_length=32)),
                ('output', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Runtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=32)),
                ('enabled', models.BooleanField(default=False)),
                ('release_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('action', models.CharField(max_length=255)),
                ('schema_version', models.PositiveIntegerField()),
                ('procedure_name', models.CharField(max_length=255)),
                ('success', models.BooleanField()),
                ('data', jsonfield.fields.JSONField()),
            ],
        ),
    ]