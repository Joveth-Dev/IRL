# Generated by Django 4.1.6 on 2023-02-16 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0029_alter_researchresearcher_research'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchresearcher',
            name='researcher',
        ),
    ]