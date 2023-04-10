# Generated by Django 4.1.6 on 2023-04-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0067_alter_research_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_description',
            new_name='project_summary',
        ),
        migrations.AddField(
            model_name='project',
            name='references',
            field=models.TextField(default='+'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sampling_site',
            field=models.TextField(default='+'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='sampling_site_image',
            field=models.ImageField(default='+', upload_to='parameter/project/images'),
            preserve_default=False,
        ),
    ]
