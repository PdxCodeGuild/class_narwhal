# Generated by Django 3.1.7 on 2021-03-04 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questions_text',
            new_name='question_text',
        ),
    ]
