# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20150717_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectblock',
            name='project',
            field=models.ForeignKey(related_name='blocks', to='portfolio.Project'),
        ),
    ]
