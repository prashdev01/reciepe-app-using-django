# Generated by Django 5.0.7 on 2024-08-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciepe_name', models.CharField(max_length=100)),
                ('reciepe_description', models.TextField()),
                ('reciepe_image', models.ImageField(upload_to='reciepe')),
            ],
        ),
    ]
