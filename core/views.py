from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Event, UserProfile, Participation, Conversation
from .forms import AddEventForm, ParticipationForm

def search(request):
    return render(request, 'search.html')

def frontpage(request):
    events = Event.objects.order_by('-created_at')
    return render(request, 'frontpage.html', {'events': events})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_type = request.POST.get('account_type', 'user')
            if account_type == 'admin':
                userprofile = UserProfile.objects.create(user=user, is_admin=True)
                userprofile.save()
            else:
                userprofile = UserProfile.objects.create(user=user)
                userprofile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

@login_required
def participateToEvent(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            participation = form.save(commit=False)
            participation.event = event
            participation.created_by = request.user
            participation.save()
            return redirect('dashboard')
    else:
        form = ParticipationForm()
    return render(request, 'participateToEvent.html', {'form': form, 'event': event})


@login_required
def addEvent(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('dashboard')
    else:        
        form = AddEventForm()
    
    return render(request, 'add_event.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'userprofile': request.user.userprofile})

@login_required
def participation_details(request, participation_id):
    participation = get_object_or_404(Participation, pk=participation_id,created_by=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            conversation = Conversation.objects.create(participation=participation, message=message, created_by=request.user)
            return redirect('participation_details', participation_id)

    return render(request, 'event_participation_details.html', {'participation': participation})

@login_required
def dashboard_event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id,created_by=request.user)
    return render(request, 'dashboard_event_details.html', {'event': event})