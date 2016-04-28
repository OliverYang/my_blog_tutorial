# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(verbose_name='Email Address', db_index=True, help_text='Your email address here', max_length=254, unique=True)),
                ('nickname', models.CharField(verbose_name='Nickname', help_text='Your nickname here', blank=True, max_length=30)),
                ('is_active', models.BooleanField(verbose_name='Active', default=True, help_text='Active or not')),
                ('create_date', models.DateTimeField(verbose_name='Create Date', default=datetime.datetime(2016, 4, 28, 6, 40, 54, 33784, tzinfo=utc), help_text='User account create date')),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, verbose_name='groups', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', blank=True, verbose_name='user permissions', related_name='user_set', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
