# Generated by Django 3.1.7 on 2021-03-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0006_urls_clicked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='short_code',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
