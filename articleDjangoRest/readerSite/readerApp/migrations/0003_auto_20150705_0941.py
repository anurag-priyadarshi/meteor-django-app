# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readerApp', '0002_auto_20150705_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation',
            field=models.ForeignKey(related_name='recommendation', default=b'2', blank=True, to='readerApp.Article'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='ref_article',
            field=models.ForeignKey(related_name='article', default=b'2', blank=True, to='readerApp.Article'),
        ),
    ]
