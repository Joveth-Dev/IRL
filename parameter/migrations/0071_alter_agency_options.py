# Generated by Django 4.1.6 on 2023-04-10 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0070_agency_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name': 'Agency', 'verbose_name_plural': 'Agencies'},
        ),
    ]
