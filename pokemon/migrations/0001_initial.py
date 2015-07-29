# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=33)),
                ('type1', models.CharField(max_length=10)),
                ('type2', models.CharField(max_length=33)),
                ('pokedex_number', models.IntegerField()),
            ],
        ),
    ]
