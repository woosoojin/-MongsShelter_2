# Generated by Django 2.1.1 on 2019-07-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_auto_20190721_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='url1',
            field=models.URLField(blank=True),
        ),
    ]
