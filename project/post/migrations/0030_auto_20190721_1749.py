# Generated by Django 2.1.1 on 2019-07-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_school_url1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to='viedo/parent'),
        ),
    ]
