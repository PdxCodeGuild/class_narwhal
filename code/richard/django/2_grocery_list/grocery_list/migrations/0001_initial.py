# Generated by Django 3.1.7 on 2021-03-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateField()),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
