# Generated by Django 5.0.3 on 2024-04-04 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databas', '0002_storebase_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storebase',
            name='completed',
        ),
    ]