# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0006_auto_20160918_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_info',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('second_name', models.CharField(max_length=20, null=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('third_name', models.CharField(max_length=20, null=True)),
                ('birth', models.DateField(null=True, blank=True)),
                ('passport', models.IntegerField(blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('salary', models.IntegerField(blank=True)),
                ('experience', models.IntegerField(blank=True)),
            ],
        ),
    ]
