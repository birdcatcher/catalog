# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('credits', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=16)),
                ('desc', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('credits', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=16)),
                ('desc', models.CharField(max_length=4096)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
    ]
