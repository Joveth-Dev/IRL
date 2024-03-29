# Generated by Django 4.1.6 on 2023-04-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0064_program_is_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_posted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='is_posted',
            field=models.BooleanField(default=False),
        ),
    ]
