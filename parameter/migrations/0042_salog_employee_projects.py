# Generated by Django 4.1.6 on 2023-04-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0041_remove_project_salog_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='salog_employee',
            name='projects',
            field=models.ManyToManyField(related_name='SALOG_employees', to='parameter.project'),
        ),
    ]
