# Generated by Django 3.2.10 on 2023-12-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20231206_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_rented',
        ),
        migrations.AddField(
            model_name='movie',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
