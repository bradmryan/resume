# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 19:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20160819_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='award',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-startdate']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-releasedate']},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['-startdate']},
        ),
    ]
