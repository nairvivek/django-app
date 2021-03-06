# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 11:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator(regex='^[A-Za-z]*$')], verbose_name='First Name')),
                ('user_last_name', models.CharField(blank=True, max_length=32, null=True, validators=[django.core.validators.RegexValidator(regex='^[A-Za-z]*$')], verbose_name='Last Name')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email')),
                ('user_dob', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('user_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('user_github', models.CharField(blank=True, max_length=100, verbose_name='Github Profile')),
                ('user_linkedin', models.CharField(blank=True, max_length=100, verbose_name='Linkedin Profile')),
                ('user_bio', models.CharField(blank=True, max_length=1000, verbose_name='Short Bio')),
                ('user_occupation', models.CharField(blank=True, max_length=100, verbose_name='Occupation')),
                ('user_nationality', models.CharField(blank=True, max_length=100, verbose_name='Nationality')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
