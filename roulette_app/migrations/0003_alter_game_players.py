# Generated by Django 4.0.5 on 2022-06-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulette_app', '0002_alter_game_players_alter_game_players_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(blank=True, null=True, related_name='players', to='roulette_app.player', verbose_name='Участвовавшие игроки'),
        ),
    ]
