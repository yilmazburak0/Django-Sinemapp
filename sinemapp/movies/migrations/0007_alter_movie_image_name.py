# Generated by Django 3.2.7 on 2022-10-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20221027_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_name',
            field=models.FileField(default='', upload_to='images/afisler'),
        ),
    ]
