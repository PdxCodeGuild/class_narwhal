# Generated by Django 3.1.7 on 2021-03-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_mymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='uploaded_files'),
        ),
    ]
