# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=75)),
                ('last_name', models.CharField(max_length=75)),
                ('email_address', models.CharField(max_length=255)),
                ('password_hash', models.CharField(max_length=32)),
                ('password_salt', models.CharField(max_length=32)),
            ],
        ),
    ]
