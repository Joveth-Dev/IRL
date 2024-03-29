# Generated by Django 4.1.6 on 2023-02-16 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0034_remove_project_salog_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.salog_employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_employee', to='parameter.project')),
            ],
        ),
    ]
