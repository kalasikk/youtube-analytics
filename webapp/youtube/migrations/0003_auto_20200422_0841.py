# Generated by Django 3.0.4 on 2020-04-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20200313_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='publishedAt',
            field=models.DateTimeField(),
        ),
    ]
