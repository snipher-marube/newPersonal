# Generated by Django 3.2.4 on 2021-07-20 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0007_rename_subscribemodel_subscribers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]
