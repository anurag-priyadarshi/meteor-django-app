# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readerApp', '0003_auto_20150705_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommendation',
            field=models.ForeignKey(related_name='recommendation', default=b'', blank=True, to='readerApp.Article'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='ref_article',
            field=models.ForeignKey(related_name='article', default=b'', blank=True, to='readerApp.Article'),
        ),
    ]
