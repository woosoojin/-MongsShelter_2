# Generated by Django 2.1.1 on 2019-07-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_auto_20190721_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='url1',
            field=models.URLField(blank=True),
        ),
    ]