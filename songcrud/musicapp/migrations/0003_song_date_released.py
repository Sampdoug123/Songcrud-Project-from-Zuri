# Generated by Django 4.1.2 on 2022-10-24 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_song_lyric'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=datetime.datetime(2022, 10, 24, 7, 39, 59, 971441)),
        ),
    ]