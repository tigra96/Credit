# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0002_auto_20160914_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
