# Generated by Django 3.1.3 on 2022-01-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20220125_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='file',
            field=models.FileField(null=b'I01\n', upload_to='%Y/%m/%d'),
        ),
    ]
