# Generated by Django 4.1.6 on 2023-04-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0058_research_equipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='equipment',
        ),
        migrations.AddField(
            model_name='research',
            name='equipment',
            field=models.ManyToManyField(related_name='equipement_researches', to='parameter.equipment'),
        ),
    ]
