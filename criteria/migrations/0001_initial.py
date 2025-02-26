# Generated by Django 5.0.6 on 2024-06-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EthicalCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('low', 'Low Priority'), ('medium', 'Medium Priority'), ('high', 'High Priority')], default='low', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('low', 'Low Priority'), ('medium', 'Medium Priority'), ('high', 'High Priority')], default='low', max_length=10)),
            ],
        ),
    ]
