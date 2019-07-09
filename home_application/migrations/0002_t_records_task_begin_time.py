# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_records_task',
            name='begin_time',
            field=models.DateTimeField(null=True, verbose_name='\u5f55\u5165\u65f6\u95f4'),
        ),
    ]
