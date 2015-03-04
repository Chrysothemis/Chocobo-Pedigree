# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chocobo',
            name='acc_source',
            field=models.CharField(max_length=1, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='cunning_source',
            field=models.CharField(max_length=1, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='end_source',
            field=models.CharField(max_length=1, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='father',
            field=models.ForeignKey(related_name='+', blank=True, to='choco.Chocobo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='mother',
            field=models.ForeignKey(related_name='+', blank=True, to='choco.Chocobo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='speed_source',
            field=models.CharField(max_length=1, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='stamina_source',
            field=models.CharField(max_length=1, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='ability_a',
            field=models.ForeignKey(related_name='+', blank=True, to='choco.Ability'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='ability_h',
            field=models.ForeignKey(related_name='+', blank=True, to='choco.Ability'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='acc_stat',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='color',
            field=models.ForeignKey(to='choco.Color', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='cunning_stat',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='end_stat',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='img_link',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='rank',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='rating',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='speed_stat',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='stamina_stat',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chocobo',
            name='weather',
            field=models.ForeignKey(to='choco.Weather', blank=True),
            preserve_default=True,
        ),
    ]
