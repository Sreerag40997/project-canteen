# Generated by Django 4.2.5 on 2023-10-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermain',
            name='User',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preorder',
            name='Time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='preorder',
            name='Type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
