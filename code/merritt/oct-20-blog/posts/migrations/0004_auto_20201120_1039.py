# Generated by Django 3.1.3 on 2020-11-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20201120_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=500),
        ),
    ]
