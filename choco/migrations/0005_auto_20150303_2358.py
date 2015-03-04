# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choco', '0004_chocobo_jockey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocobo',
            name='color',
            field=models.ForeignKey(blank=True, to='choco.Color', null=True),
            preserve_default=True,
        ),
    ]
