# Generated by Django 5.1 on 2024-10-01 21:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options_alter_project_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]