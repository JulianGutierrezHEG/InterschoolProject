from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import JSONParser

from base.models import Place, Event
from base.serializers import PlaceSerializer, EventSerializer
# Create your views here.


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

