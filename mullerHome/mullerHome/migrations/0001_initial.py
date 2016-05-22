# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('blog_content', models.TextField()),
                ('blog_description', models.CharField(max_length=200)),
                ('blog_thumbnail', models.URLField()),
            ],
        ),
    ]