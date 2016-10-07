# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='clients',
            name='age',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='author',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='job',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='age',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='current',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='history',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='outstanding',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='summ',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='time',
        ),
        migrations.AddField(
            model_name='clients',
            name='birth_day',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='third_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Last_Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Repayment_Period',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Salary',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Second_Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Work_Experience',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='childrens',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='published_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
