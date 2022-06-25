from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Player, Game
from .serializers import PlayerSerializer, GameSerializer, PlayerStatisticsSerializer, GameStatisticsSerializer
from .logic import get_spins


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.order_by('-id')
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # берем из модели game дефолтный список ячеек
        current_array = serializer.data['array']

        # помещаем в функцию рулетки
        get_spins(current_array)

        # определяем последний созданный раунд
        game = Game.objects.order_by('id').last()

        # присваиваем новый список модели game после первого хода
        game.array = current_array

        # добавляем игрока начавшего раунд в список участвоваших
        game.players_array.append(request.user.id)

        # добавляем количество сыгранных раундов игроку
        player = Player.objects.get(id=request.user.id)
        player.rounds_qty += 1

        # добавляем в статистику игроку прокрут рулетки
        player.spins += 1

        # обновляем статистику среднее количество прокрутов игрока за раунд
        player.average_spin = player.spins // player.rounds_qty

        # подсчитываем количество игроков участвовавших в раунде
        game.players_qty = len(game.players_array)

        game.save()
        player.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        # определяем id игры
        game = Game.objects.get(id=kwargs.get('pk'))
        # определяем игрока
        player = Player.objects.get(id=request.user.id)

        # проверяем активная ли еще игра
        if game.is_finished:
            return Response(serializer.data)
        else:
            # делаем очередной ход в раунде
            # если сделан 11 ход - игра заканчивается
            if get_spins(game.array) == 11:
                game.is_finished = True

            # если игрок не участвовал ранее в раунде, то добавляем его в список участвовавших
            # добавляем ему игру в статистику
            if request.user.id not in game.players_array:
                game.players_array.append(request.user.id)
                player.rounds_qty += 1

            # добавляем в статистику игроку прокрут рулетки
            player.spins += 1

            # обновляем статистику среднее количество прокрутов игрока за раунд
            player.average_spin = player.spins // player.rounds_qty

            # обновляем общее количество игроков участвовавших в игре
            game.players_qty = len(game.players_array)

            game.save()
            player.save()

        return Response(serializer.data)


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.order_by('-rounds_qty')
    serializer_class = PlayerSerializer
    permission_classes = (IsAuthenticated, )


class GameStatisticsViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameStatisticsSerializer


class PlayersStatisticsViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.order_by('-rounds_qty')
    serializer_class = PlayerStatisticsSerializer
