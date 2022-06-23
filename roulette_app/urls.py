from django.urls import path, include
from .views import GameViewSet, PlayerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('games', GameViewSet, basename='games')
router.register('games/<int:pk>/', GameViewSet, basename='games')
router.register('players', PlayerViewSet, basename='players')
router.register('players/<int:pk>/', PlayerViewSet, basename='players')

urlpatterns = [
    path('api/', include(router.urls)),
]
