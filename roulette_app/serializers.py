from rest_framework import serializers
from .models import Player, Game


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'rounds_qty', 'average_spin']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'players_qty', 'array']
