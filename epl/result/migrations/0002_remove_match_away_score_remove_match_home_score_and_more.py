# Generated by Django 5.0.3 on 2024-03-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='away_score',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_score',
        ),
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
