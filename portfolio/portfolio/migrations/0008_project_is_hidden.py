# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_projectblock_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]
