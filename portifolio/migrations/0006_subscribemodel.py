# Generated by Django 3.2.4 on 2021-07-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0005_delete_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeModel',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
