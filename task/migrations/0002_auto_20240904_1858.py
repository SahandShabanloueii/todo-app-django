# Generated by Django 3.2.7 on 2024-09-04 18:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='category',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.CASCADE, to='task.category'),
        ),
        migrations.AlterField(
            model_name='todotask',
            name='created',
            field=models.DateField(default=datetime.datetime(2024, 9, 4, 18, 58, 51, 890079, tzinfo=utc)),
        ),
    ]
