# Generated by Django 2.1.1 on 2019-08-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0043_auto_20190802_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
