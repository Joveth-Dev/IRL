# Generated by Django 4.1.6 on 2023-02-16 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0030_remove_researchresearcher_researcher'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='researcher_research',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='researcher', to='parameter.researchresearcher'),
        ),
    ]
