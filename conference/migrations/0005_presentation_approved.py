# Generated by Django 3.1.7 on 2021-04-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0004_auto_20210401_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
