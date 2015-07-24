# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20150719_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'media/portfolio/projects/images', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'media/portfolio/projects/logos', blank=True),
        ),
        migrations.AlterField(
            model_name='projectblock',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'media/portfolio/projects/images', blank=True),
        ),
    ]
