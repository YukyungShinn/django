# Generated by Django 3.1.3 on 2022-01-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
