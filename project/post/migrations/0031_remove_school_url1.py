# Generated by Django 2.1.1 on 2019-07-21 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0030_auto_20190721_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='url1',
        ),
    ]
