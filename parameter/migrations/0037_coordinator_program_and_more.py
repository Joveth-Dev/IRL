# Generated by Django 4.1.6 on 2023-04-07 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parameter', '0036_rename_description_project_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('executive_summary', models.TextField()),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.coordinator')),
            ],
        ),
        migrations.RemoveField(
            model_name='researchresearcher',
            name='research',
        ),
        migrations.RemoveField(
            model_name='researchresearcher',
            name='researcher',
        ),
        migrations.AddField(
            model_name='research',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parameter.project'),
        ),
        migrations.AddField(
            model_name='research',
            name='researchers',
            field=models.ManyToManyField(related_name='researches', to='parameter.researcher'),
        ),
        migrations.DeleteModel(
            name='ProjectEmployee',
        ),
        migrations.DeleteModel(
            name='ResearchResearcher',
        ),
        migrations.AddField(
            model_name='project',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parameter.program'),
        ),
    ]
