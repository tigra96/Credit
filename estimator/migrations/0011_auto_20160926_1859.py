# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0010_auto_20160922_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_job',
            fields=[
                ('Id', models.AutoField(serialize=False, primary_key=True)),
                ('id_client', models.IntegerField(blank=True)),
                ('work_place', models.CharField(max_length=20, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='surname',
        ),
        migrations.RemoveField(
            model_name='client_info',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='client_info',
            name='salary',
        ),
        migrations.AddField(
            model_name='client_info',
            name='id_author',
            field=models.IntegerField(null=True),
        ),
    ]
