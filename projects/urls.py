from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/brawlers', BrawlerViewSet, 'projects')
urlpatterns = router.urls
