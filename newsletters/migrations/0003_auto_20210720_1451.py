# Generated by Django 3.2.4 on 2021-07-20 14:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_rename_newletterusers_newletteruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='newletteruser',
            name='conf_num',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newletteruser',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newletteruser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]