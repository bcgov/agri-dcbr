# Generated by Django 2.2 on 2019-09-20 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20190919_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association_membership',
            name='assoc_URL',
        ),
        migrations.RemoveField(
            model_name='association_membership',
            name='membership_num',
        ),
    ]