# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150712_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectblock',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'portfolio/projects/images', blank=True),
        ),
    ]
