import json
from django.db.models import Q
from django.http import JsonResponse
from .models import *

def api_search(request):
    eventslist = []
    data = json.loads(request.body)
    query = data['query']
    event_name = data['title']

    events = Event.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(long_description__icontains=query) | Q(location__icontains=query))

    if event_name:
        events = events.filter(event_name = event_name)
    for event in events:
        obj = {
            'id' : event.id,
            'title': event.title,
            'url': '/events/%s' % event.id
        }
        eventslist.append(obj)
    return JsonResponse({'events': eventslist})