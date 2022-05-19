from rest_framework import serializers
from base.models import Place, Event


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('__all__')