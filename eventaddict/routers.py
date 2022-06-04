from rest_framework import routers
from core.viewsets import PlaceViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r'place', PlaceViewSet)
router.register(r'event', EventViewSet)
