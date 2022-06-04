from django import forms
from .models import Event, Participation

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }