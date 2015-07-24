# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('ptype', models.CharField(max_length=64, verbose_name='Project type')),
                ('client', models.CharField(max_length=64)),
                ('date', models.DateField(verbose_name='End date of project')),
                ('short', models.TextField(verbose_name='Short description')),
                ('readmore', models.CharField(max_length=64, verbose_name='Read more link text')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ProjectBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=255, null=True, blank=True)),
                ('tagline', models.CharField(max_length=255, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'portfolio/projects/images')),
                ('order', models.IntegerField(default=10)),
                ('project', models.ForeignKey(to='portfolio.Project')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='portfolio.Tag', null=True, blank=True),
        ),
    ]
