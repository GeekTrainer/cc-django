# Generated by Django 3.1.7 on 2021-04-01 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0003_auto_20210401_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speaker',
            old_name='instragram',
            new_name='instagram',
        ),
    ]
