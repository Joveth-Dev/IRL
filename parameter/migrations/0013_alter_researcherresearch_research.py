# Generated by Django 4.1.6 on 2023-02-11 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0012_alter_researcherresearch_research'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcherresearch',
            name='research',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='research', to='parameter.research'),
        ),
    ]
