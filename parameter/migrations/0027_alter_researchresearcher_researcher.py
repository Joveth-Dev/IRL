# Generated by Django 4.1.6 on 2023-02-16 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0026_alter_researchresearcher_research'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchresearcher',
            name='researcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.researcher', unique=True),
        ),
    ]
