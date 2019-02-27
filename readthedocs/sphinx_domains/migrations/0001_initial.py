# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-27 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('builds', '0006_add_config_field'),
        ('projects', '0040_increase_path_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SphinxDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('commit', models.CharField(max_length=255, null=True, verbose_name='Commit')),
                ('domain', models.CharField(max_length=255, verbose_name='Domain')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('display_name', models.CharField(max_length=255, verbose_name='Display Name')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('doc_name', models.CharField(max_length=255, verbose_name='Doc Name')),
                ('anchor', models.CharField(max_length=255, verbose_name='Anchor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sphinx_domains', to='projects.Project')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sphinx_domains', to='builds.Version', verbose_name='Version')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
