# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 17:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default=b'', max_length=200)),
                ('email_address', models.EmailField(blank=True, default=b'', max_length=500)),
                ('phone', models.BigIntegerField(default=0)),
                ('addressline1', models.CharField(blank=True, default=b'', max_length=200)),
                ('addressline2', models.CharField(blank=True, default=b'', max_length=200)),
                ('postcode', models.CharField(blank=True, default=b'', max_length=10)),
                ('account_created_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
