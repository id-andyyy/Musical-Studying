# Generated by Django 3.2 on 2021-05-06 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_alter_songs_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='songs',
            table='all_songs',
        ),
    ]
