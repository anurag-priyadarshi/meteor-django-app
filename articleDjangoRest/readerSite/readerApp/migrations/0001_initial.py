# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'Publication Date')),
                ('category', models.CharField(max_length=50)),
                ('imageMain', models.ImageField(upload_to=b'images')),
                ('imageAdditional', models.ImageField(upload_to=b'images')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]
