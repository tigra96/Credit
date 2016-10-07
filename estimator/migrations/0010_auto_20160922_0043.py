# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0009_auto_20160919_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='surname',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('second_name', models.CharField(null=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='estimate',
            name='passport',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
