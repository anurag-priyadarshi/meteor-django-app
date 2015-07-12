# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('readerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='imageAdditional',
            field=models.ImageField(upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='imageMain',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(verbose_name=b'Publication Date'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='recommendation',
            field=models.ForeignKey(related_name='recommendation', default=b'1', blank=True, to='readerApp.Article'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='ref_article',
            field=models.ForeignKey(related_name='article', default=b'1', blank=True, to='readerApp.Article'),
        ),
    ]
