# Generated by Django 4.0.5 on 2022-06-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulette_app', '0008_remove_game_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
