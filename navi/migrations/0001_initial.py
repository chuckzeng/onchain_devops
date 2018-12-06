# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='navi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('description', models.CharField(max_length=50, verbose_name='\u63cf\u8ff0')),
                ('url', models.URLField(verbose_name='\u7f51\u7ad9')),
            ],
        ),
    ]
