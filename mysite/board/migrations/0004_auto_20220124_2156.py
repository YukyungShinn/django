# Generated by Django 3.1.3 on 2022-01-24 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_uploadfile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.AddField(
            model_name='review',
            name='file',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
