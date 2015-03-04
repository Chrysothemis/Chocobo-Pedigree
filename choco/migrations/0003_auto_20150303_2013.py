# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choco', '0002_auto_20150303_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='chocobo',
            name='pedigree',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ability',
            name='img1',
            field=models.ImageField(upload_to=b'choco\\static'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='ability_a',
            field=models.ForeignKey(related_name='+', blank=True, to='choco.Ability', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='ability_h',
            field=models.ForeignKey(related_name='+', blank=True, to='choco.Ability', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='acc_source',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='acc_stat',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='cunning_source',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='cunning_stat',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='end_source',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='end_stat',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='img_link',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='rank',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='speed_source',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='speed_stat',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='stamina_source',
            field=models.CharField(max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='stamina_stat',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='weather',
            field=models.ForeignKey(blank=True, to='choco.Weather', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='color',
            name='img',
            field=models.ImageField(upload_to=b'choco\\static'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weather',
            name='img1',
            field=models.ImageField(upload_to=b'choco\\static'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weather',
            name='img2',
            field=models.ImageField(upload_to=b'choco\\static'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='weather',
            name='img3',
            field=models.ImageField(upload_to=b'choco\\static'),
            preserve_default=True,
        ),
    ]
