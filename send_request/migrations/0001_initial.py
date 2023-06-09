# Generated by Django 4.2 on 2023-04-17 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SendModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=50, verbose_name='form name')),
                ('token', models.CharField(max_length=255, verbose_name='token of discord account')),
                ('channel_id', models.CharField(max_length=25, verbose_name='ID of discord channel')),
                ('text', models.TextField(max_length=5000, verbose_name='text for messege')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'form to send',
                'verbose_name_plural': 'forms to send',
            },
        ),
        migrations.CreateModel(
            name='URLarray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL of picture')),
                ('sendmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_request.sendmodel')),
            ],
            options={
                'verbose_name': 'URL for send model',
                'verbose_name_plural': 'URLs for send model',
            },
        ),
    ]
