# Generated by Django 3.1.7 on 2021-03-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='bought',
            field=models.BooleanField(default=False),
        ),
    ]
