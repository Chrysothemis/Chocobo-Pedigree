# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('img1', models.ImageField(upload_to=b'uploads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chocobo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('speed_stars', models.IntegerField()),
                ('acc_stars', models.IntegerField()),
                ('end_stars', models.IntegerField()),
                ('stamina_stars', models.IntegerField()),
                ('cunning_stars', models.IntegerField()),
                ('speed_stat', models.IntegerField()),
                ('acc_stat', models.IntegerField()),
                ('end_stat', models.IntegerField()),
                ('stamina_stat', models.IntegerField()),
                ('cunning_stat', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
                ('rank', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('img_link', models.CharField(max_length=200)),
                ('ability_a', models.ForeignKey(related_name='+', to='choco.Ability')),
                ('ability_h', models.ForeignKey(related_name='+', to='choco.Ability')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to=b'uploads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('img1', models.ImageField(upload_to=b'uploads')),
                ('img2', models.ImageField(upload_to=b'uploads')),
                ('img3', models.ImageField(upload_to=b'uploads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chocobo',
            name='color',
            field=models.ForeignKey(to='choco.Color'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chocobo',
            name='weather',
            field=models.ForeignKey(to='choco.Weather'),
            preserve_default=True,
        ),
    ]
