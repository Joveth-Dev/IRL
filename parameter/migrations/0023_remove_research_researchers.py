# Generated by Django 4.1.6 on 2023-02-16 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0022_researchresearcher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='researchers',
        ),
    ]