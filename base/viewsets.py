from rest_framework import viewsets,filters
from .models import Place, Event
from .serializers import PlaceSerializer, EventSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('place_id', 'place_name','place_address')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('event_id', 'event_name','event_description')