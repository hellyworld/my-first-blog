# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
            preserve_default=False,
        ),
    ]
