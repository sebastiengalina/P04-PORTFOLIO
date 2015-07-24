# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20150722_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectblock',
            name='caption',
            field=models.TextField(null=True, blank=True),
        ),
    ]
