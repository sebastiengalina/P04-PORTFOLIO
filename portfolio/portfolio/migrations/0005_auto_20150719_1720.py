# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20150717_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'portfolio/projects/images', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'porfolio/projects/logos', blank=True),
        ),
    ]
