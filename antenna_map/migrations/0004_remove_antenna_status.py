# Generated by Django 4.2 on 2023-04-12 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antenna_map', '0003_alter_antenna_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antenna',
            name='status',
        ),
    ]
