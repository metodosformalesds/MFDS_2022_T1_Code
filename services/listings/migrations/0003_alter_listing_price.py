# Generated by Django 4.1.3 on 2022-11-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_no_of_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
