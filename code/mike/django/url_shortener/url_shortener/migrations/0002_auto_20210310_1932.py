# Generated by Django 3.1.7 on 2021-03-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='short_code',
            field=models.URLField(blank=True, null=True),
        ),
    ]
