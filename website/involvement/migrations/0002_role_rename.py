# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 15:51
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('involvement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Function', 'Role'),
        migrations.RenameField('Position', 'function', 'role'),

        migrations.RenameField('Position', 'commencement', 'recruitment_start'),
        migrations.RenameField('Position', 'deadline', 'recruitment_end'),

        # Automatically Generated
        migrations.AlterModelOptions(
            name='role',
            options={'default_permissions': (),
                     'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'default_permissions': (), 'permissions': (
            ('admin', 'Can administrate the recruitment process'),),
                     'verbose_name_plural': 'Teams'},
        ),
        migrations.AlterField(
            model_name='role',
            name='archived',
            field=models.BooleanField(default=False,
                                      help_text='Hide the role from menus',
                                      verbose_name='Archived'),
        ),
        migrations.AlterField(
            model_name='role',
            name='description_en',
            field=models.TextField(blank=True,
                                   help_text='Enter a description of the role',
                                   verbose_name='English role description'),
        ),
        migrations.AlterField(
            model_name='role',
            name='description_sv',
            field=models.TextField(blank=True,
                                   help_text='Enter a description of the role',
                                   verbose_name='Swedish role description'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name_en',
            field=models.CharField(help_text='Enter the name of the role',
                                   max_length=255,
                                   verbose_name='English role name'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name_sv',
            field=models.CharField(help_text='Enter the name of the role',
                                   max_length=255,
                                   verbose_name='Swedish role name'),
        ),
        migrations.AlterField(
            model_name='role',
            name='official',
            field=models.BooleanField(default=False,
                                      help_text='This is an official role',
                                      verbose_name='Official'),
        ),
        migrations.AlterField(
            model_name='role',
            name='team',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=models.deletion.PROTECT,
                                    related_name='roles',
                                    to='involvement.Team'),
        ),
        migrations.AlterField(
            model_name='position',
            name='recruitment_start',
            field=models.DateField(default=datetime.date.today,
                                   verbose_name='Start of recruitment'),
        ),
    ]