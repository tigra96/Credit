# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, verbose_name='e-mail', max_length=254)),
                ('age', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('childrens', models.BooleanField()),
                ('job', models.BooleanField()),
                ('experience', models.IntegerField(blank=True)),
                ('amount_of_credit', models.IntegerField()),
                ('payout_period', models.IntegerField()),
                ('credits_history', models.IntegerField()),
                ('number_of_current_credits', models.IntegerField()),
                ('number_of_outstanding_credits', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary', models.IntegerField()),
                ('age', models.IntegerField()),
                ('summ', models.IntegerField()),
                ('time', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('history', models.IntegerField()),
                ('current', models.IntegerField()),
                ('outstanding', models.IntegerField()),
            ],
        ),
    ]
