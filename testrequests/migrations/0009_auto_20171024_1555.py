# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrequests', '0008_auto_20171024_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='barcode_image',
            field=models.ImageField(blank=True, default='/static/barcodes/<django.db.models.fields.CharField>.png', null=True, upload_to=''),
        ),
    ]
