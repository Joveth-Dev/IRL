# Generated by Django 4.1.6 on 2023-04-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0046_alter_salog_employee_date_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.CharField(choices=[('L', 'Local'), ('N', 'National'), ('I', 'International')], max_length=1),
        ),
    ]