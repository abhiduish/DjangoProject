# Generated by Django 3.1.7 on 2021-03-01 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 13, 16, 11, 659233, tzinfo=utc), verbose_name='date published'),
        ),
    ]