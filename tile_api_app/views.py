from rest_framework import routers
from .serializers import TaskViewSet, TileViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tiles', TileViewSet)