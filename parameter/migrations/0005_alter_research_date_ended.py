# Generated by Django 4.1.6 on 2023-02-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0004_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='date_ended',
            field=models.DateField(blank=True, null=True),
        ),
    ]
