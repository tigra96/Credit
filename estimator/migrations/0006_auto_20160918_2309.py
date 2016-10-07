# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0005_auto_20160918_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='result',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
