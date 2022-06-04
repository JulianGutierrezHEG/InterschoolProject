from django.urls import path, include
from .views import *
from .api import *

urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    path('', dashboard, name='dashboard'),
    path('add/', addEvent, name='addEvent'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('<int:event_id>/participateToEvent/', participateToEvent, name='participateToEvent'),
    path('participation/<int:participation_id>/', participation_details, name='participation_details'),
    path('event/<int:event_id>/', dashboard_event_details, name='dashboard_event_details'),
]
