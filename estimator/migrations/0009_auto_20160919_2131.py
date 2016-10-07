# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0008_client_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_info',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='client_info',
            name='email',
            field=models.EmailField(max_length=254, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client_info',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client_info',
            name='passport',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client_info',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
