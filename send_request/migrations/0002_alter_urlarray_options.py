# Generated by Django 4.2 on 2023-04-08 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urlarray',
            options={'verbose_name': 'URL for send model', 'verbose_name_plural': 'URLs for send model'},
        ),
    ]
