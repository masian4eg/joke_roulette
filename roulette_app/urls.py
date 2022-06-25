from django.urls import path, include
from .views import GameViewSet, PlayerViewSet, PlayersStatisticsViewSet, GameStatisticsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('games', GameViewSet, basename='games')
router.register('games/<int:pk>', GameViewSet)
router.register('games_statistics', GameStatisticsViewSet, basename='games_statistics')
router.register('players', PlayerViewSet, basename='players')
router.register('players/<int:pk>', PlayerViewSet)
router.register('players_statistics', PlayersStatisticsViewSet, basename='players_statistics')


urlpatterns = [
    path('api/', include(router.urls)),
]
