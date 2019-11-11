# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-08 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors_app', '0002_authors_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='author', to='book_authors_app.Books'),
        ),
    ]