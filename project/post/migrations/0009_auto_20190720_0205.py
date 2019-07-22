# Generated by Django 2.1.1 on 2019-07-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20190720_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/revewing')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]