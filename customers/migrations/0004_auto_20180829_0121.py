# Generated by Django 2.1 on 2018-08-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20180827_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers_profile',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='customers_profile',
            name='shaba',
        ),
    ]