# Generated by Django 4.0.1 on 2022-01-18 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='cnt',
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
