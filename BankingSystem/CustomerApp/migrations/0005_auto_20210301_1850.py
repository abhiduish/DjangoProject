# Generated by Django 3.1.7 on 2021-03-01 13:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0004_auto_20210301_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('account_no', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=10)),
                ('balance', models.FloatField(default=0.0)),
                ('address', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 3, 1, 13, 20, 17, 715648, tzinfo=utc), verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
