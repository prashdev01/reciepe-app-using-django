# Generated by Django 5.0.7 on 2024-08-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepe',
            name='reciepe_image',
            field=models.ImageField(upload_to='reciepe/'),
        ),
    ]
