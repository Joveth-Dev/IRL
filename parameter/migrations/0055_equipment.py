# Generated by Django 4.1.6 on 2023-04-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0054_research_linkage_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='parameter/equipment/image')),
            ],
        ),
    ]
