# Generated by Django 3.2.7 on 2024-09-06 10:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20240904_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='created',
            field=models.DateField(default=datetime.datetime(2024, 9, 6, 10, 55, 35, 846995, tzinfo=utc)),
        ),
    ]
