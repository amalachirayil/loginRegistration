# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg_app', '0002_auto_20170628_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
