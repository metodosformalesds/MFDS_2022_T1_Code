# Generated by Django 4.1.3 on 2022-11-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_user_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=models.CharField(default='', max_length=200),
        ),
    ]
