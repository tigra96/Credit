# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0007_client_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_history',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Id_client', models.IntegerField(blank=True)),
                ('start_credit', models.DateField(blank=True, null=True)),
                ('finish_credit', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True)),
                ('number_of_delays', models.IntegerField(blank=True)),
                ('status', models.CharField(null=True, max_length=20)),
            ],
        ),
    ]
