# Generated by Django 4.2 on 2023-05-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InitialCommitRecord',
            fields=[
                ('adlobj_id', models.IntegerField(primary_key=True, serialize=False)),
                ('initial_commit', models.BooleanField()),
                ('version', models.IntegerField()),
                ('svndate', models.DateTimeField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=256, null=True)),
                ('revision', models.IntegerField(blank=True, null=True)),
                ('svn_path', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
