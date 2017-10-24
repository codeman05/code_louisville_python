# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('manager', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text='XXX-XXX-XXXX', max_length=12)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testrequests.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.CharField(max_length=30)),
                ('model_number', models.CharField(max_length=30)),
                ('part_number', models.CharField(blank=True, max_length=30, null=True)),
                ('date_code', models.CharField(blank=True, max_length=30, null=True)),
                ('nominal_height', models.PositiveIntegerField(blank=True, help_text='inches', null=True)),
                ('nominal_width', models.PositiveIntegerField(blank=True, help_text='inches', null=True)),
                ('nominal_depth', models.PositiveIntegerField(blank=True, help_text='inches', null=True)),
                ('pleat_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('pocket_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('media_type', models.CharField(blank=True, max_length=30, null=True)),
                ('adhesive_type', models.CharField(blank=True, max_length=30, null=True)),
                ('adhesive_amount', models.CharField(blank=True, max_length=30, null=True)),
                ('disposal', models.BooleanField(default=False)),
                ('quote_number', models.CharField(blank=True, max_length=30, null=True)),
                ('po_number', models.CharField(blank=True, max_length=30, null=True)),
                ('air_flow_rate', models.PositiveIntegerField()),
                ('test_dust', models.CharField(blank=True, choices=[('IF', 'ISO Fine'), ('IC', 'ISO Coarse'), ('A', 'ASHRAE')], max_length=2, null=True)),
                ('final_resistance', models.PositiveIntegerField(blank=True, help_text='in W.G.', null=True)),
                ('dust_feed_rate', models.PositiveIntegerField(blank=True, help_text='(gms / MCF)', null=True)),
                ('initial_loading_pressure', models.PositiveIntegerField(blank=True, help_text='in W.G.', null=True)),
                ('hi_pulse_pressure', models.PositiveIntegerField(blank=True, help_text='in W.G.', null=True)),
                ('lo_pulse_pressure', models.PositiveIntegerField(blank=True, help_text='in W.G.', null=True)),
                ('pulse_ms_on', models.PositiveIntegerField(blank=True, help_text='in milliseconds', null=True)),
                ('pulse_ms_off', models.PositiveIntegerField(blank=True, help_text='in milliseconds', null=True)),
                ('pulse_pressure', models.PositiveIntegerField(blank=True, help_text='in W.G.', null=True)),
                ('not_to_exceed_pressure', models.PositiveIntegerField(blank=True, help_text='in W.G.', null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testrequests.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(blank=True, max_length=7, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testrequests.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='test',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testrequests.TestType'),
        ),
    ]
