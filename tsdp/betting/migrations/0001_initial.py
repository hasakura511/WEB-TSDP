# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-25 04:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value1', models.TextField()),
                ('value2', models.TextField()),
                ('mcdate', models.TextField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('components', models.TextField()),
                ('triggers', models.TextField()),
                ('mcdate', models.TextField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('selection', models.TextField()),
                ('v4futures', models.TextField()),
                ('v4mini', models.TextField()),
                ('v4micro', models.TextField()),
                ('componentloc', models.TextField(default=b'[{"c0": "Off"}, {"c1": "RiskOn"}, {"c2": "RiskOff"}, {"c3": "LowestEquity"}, {"c4": "HighestEquity"}, {"c5": "AntiHighestEquity"}, {"c6": "Anti50/50"}, {"c7": "Seasonality"}, {"c8": "Anti-Seasonality"}, {"c9": "Previous"}, {"c10": "None"}, {"c11": "Anti-Previous"}, {"c12": "None"}, {"c13": "None"}, {"c14": "None"}]')),
                ('mcdate', models.TextField()),
                ('timestamp', models.IntegerField()),
            ],
        ),
    ]