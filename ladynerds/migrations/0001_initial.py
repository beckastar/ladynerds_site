# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('city', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=40)),
                ('twitter', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=40)),
                ('past_companies', models.CharField(max_length=50)),
                ('freelancer', models.BooleanField()),
                ('languages', models.CharField(max_length=40)),
                ('frameworks', models.CharField(max_length=40)),
                ('year_graduated', models.IntegerField()),
                ('season_graduated', models.CharField(max_length=20)),
                ('looking_for_job', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=20, choices=[(b'Full Stack', b'Full_stack'), (b'Front end', b'Front_end'), (b'Back_end', b'Back_end'), (b'UI/UX', b'UI_UX'), (b'Design', b'Design'), (b'Devops', b'Devops'), (b'Sys_admin', b'Sys_admin'), (b'Build_and_release', b'Build_release'), (b'Project_manager', b'Project_manager'), (b'Support_eng', b'Support_eng'), (b'Manager', b'Manager'), (b'QA', b'QA'), (b'Security', b'Security'), (b'Dev_evangelist', b'Dev_evangelist'), (b'Other', b'Other')])),
                ('position_other', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
