# Generated by Django 2.1.1 on 2019-07-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20190720_0205'),
    ]

    operations = [
        migrations.CreateModel(
            name='School1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title3', models.CharField(max_length=100)),
                ('v_url', models.URLField()),
                ('description4', models.CharField(max_length=1000)),
            ],
        ),
    ]
