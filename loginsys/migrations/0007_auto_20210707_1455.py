# Generated by Django 3.2 on 2021-07-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0006_alter_profiles_was_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='last_songs',
            field=models.TextField(blank=True, verbose_name='последние песни'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='was_online',
            field=models.DateTimeField(auto_now_add=True, verbose_name='последняя активность'),
        ),
    ]
