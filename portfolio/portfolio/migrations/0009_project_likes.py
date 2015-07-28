# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
