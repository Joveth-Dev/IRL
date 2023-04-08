# Generated by Django 4.1.6 on 2023-04-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0059_remove_research_equipment_research_equipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='equipment',
        ),
        migrations.AddField(
            model_name='research',
            name='equipments',
            field=models.ManyToManyField(related_name='equipment_researches', to='parameter.equipment'),
        ),
    ]
