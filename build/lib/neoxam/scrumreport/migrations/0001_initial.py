# Generated by Django 3.2.19 on 2023-05-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_id', models.IntegerField(unique=True)),
                ('key', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=1023)),
                ('timespent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('epic_color', models.CharField(blank=True, max_length=32, null=True)),
                ('epic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scrumreport.issue')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_id', models.IntegerField(unique=True)),
                ('key', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Scrum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_id', models.IntegerField(unique=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_id', models.IntegerField(unique=True)),
                ('key', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('closed', models.BooleanField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('complete_date', models.DateTimeField(blank=True, null=True)),
                ('completed_issues', models.ManyToManyField(related_name='completed_in_sprint', to='scrumreport.Issue')),
                ('incompleted_issues', models.ManyToManyField(related_name='incompleted_in_sprint', to='scrumreport.Issue')),
                ('punted_issues', models.ManyToManyField(related_name='punted_from_sprint', to='scrumreport.Issue', verbose_name='Issues that are no longer in the sprint')),
                ('scrum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrumreport.scrum')),
            ],
        ),
        migrations.CreateModel(
            name='NxUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldap_username', models.CharField(max_length=255, unique=True)),
                ('ldap_password', models.CharField(max_length=255)),
                ('current_scrum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrumreport.scrum')),
            ],
        ),
    ]