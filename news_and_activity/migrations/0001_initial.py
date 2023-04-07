# Generated by Django 4.1.6 on 2023-04-07 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parameter', '0048_remove_news_project_remove_news_research_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('details', models.TextField()),
                ('category', models.CharField(choices=[('L', 'Local'), ('N', 'National'), ('I', 'International')], max_length=1)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_expired', models.DateTimeField()),
                ('status', models.CharField(choices=[('D', 'Display'), ('H', 'Hidden')], max_length=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.project')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.research')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('activity_type', models.CharField(choices=[('C', 'Conference'), ('L', 'Lecture'), ('T', 'Training'), ('F', 'Forum'), ('M', 'Meeting')], max_length=1)),
                ('date_started', models.DateField()),
                ('date_ended', models.DateField()),
                ('duration', models.SmallIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.project')),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parameter.research')),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
    ]