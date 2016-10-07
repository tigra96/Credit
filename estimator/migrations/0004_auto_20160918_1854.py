# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0003_auto_20160914_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='childrens',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='result',
            field=models.BooleanField(choices=[(True, 'Выдали'), (False, 'Не выдали')]),
        ),
    ]
