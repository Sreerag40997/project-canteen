# Generated by Django 4.2.5 on 2023-12-28 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_ordermain_user_preorder_time_preorder_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todaymenu',
            name='Food',
        ),
    ]
