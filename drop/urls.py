from rest_framework import routers
from .api import DropViewSet

router = routers.DefaultRouter()
router.register('api/drop', DropViewSet, 'drop')

urlpatterns = router.urls