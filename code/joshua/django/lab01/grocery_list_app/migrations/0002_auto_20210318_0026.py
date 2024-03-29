# Generated by Django 3.1.7 on 2021-03-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
