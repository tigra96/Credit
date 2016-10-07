# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0004_auto_20160918_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='result',
            field=models.CharField(max_length=20),
        ),
    ]
