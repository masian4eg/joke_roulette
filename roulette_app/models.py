from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False, verbose_name='Имя игрока')
    rounds_qty = models.PositiveIntegerField(default=0, verbose_name='Количество сыгранных раундов')
    spins = models.IntegerField(default=0, verbose_name='Всего сделано прокручиваний рулетки')
    average_spin = models.PositiveIntegerField(default=0, verbose_name='Среднее количество вращений')
    game = models.ManyToManyField('Game', verbose_name='Участвовал в играх')

    def __str__(self):
        return f'{self.pk} {self.name}'


class Game(models.Model):
    players_qty = models.IntegerField(null=True, blank=True, verbose_name='Количество игроков')
    players_array = ArrayField(base_field=models.IntegerField(), default=[], null=True)
    array = ArrayField(
        base_field=models.PositiveIntegerField(), default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], null=True, blank=True
    )
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f'#{self.pk}'
