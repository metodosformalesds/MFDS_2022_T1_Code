# Generated by Django 4.1.3 on 2022-11-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='no_of_rating',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='total_rating',
        ),
    ]
