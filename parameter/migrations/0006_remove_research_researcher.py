# Generated by Django 4.1.6 on 2023-02-11 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0005_alter_research_date_ended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='researcher',
        ),
    ]
