# -*- coding: utf-8 -*-
# Generated by Django 3.1 on 2021-03-28 16:10
from __future__ import unicode_literals

from django.db import migrations

from ..db.db_views import PAYMENTS_BY_LOAN_DB_VIEW


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(PAYMENTS_BY_LOAN_DB_VIEW),
    ]