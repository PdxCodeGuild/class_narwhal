# Generated by Django 3.1.7 on 2021-03-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0004_auto_20210310_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='short_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]