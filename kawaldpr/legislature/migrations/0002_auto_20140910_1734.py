# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import ckeditor.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('legislature', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('reference', models.TextField(null=True, blank=True)),
                ('published', models.BooleanField(default=False)),
                ('legislature', models.ForeignKey(to='legislature.Legislature')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='legislature',
            name='area',
            field=models.ForeignKey(blank=True, to='legislature.Area', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='facebook',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='fraction',
            field=models.ForeignKey(blank=True, to='legislature.Fraction', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='incumbent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='last_Education_alert',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='last_education',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='linkedin',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='organization_work',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='organization_work_alert',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='sex',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Man'), (2, b'Woman')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='slug',
            field=autoslug.fields.AutoSlugField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='track_record',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='track_record_alert',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislature',
            name='twitter',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medium',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medium',
            name='reference',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medium',
            name='slug',
            field=autoslug.fields.AutoSlugField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
