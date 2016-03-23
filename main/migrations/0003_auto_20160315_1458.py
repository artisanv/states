# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160313_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCapital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('population', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital',
        ),
        migrations.RemoveField(
            model_name='state',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='longtitude',
        ),
        migrations.RemoveField(
            model_name='state',
            name='population',
        ),
        migrations.AddField(
            model_name='statecapital',
            name='state',
            field=models.OneToOneField(null=True, to='main.State'),
        ),
    ]
