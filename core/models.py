from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='userprofile', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

#Create a user profile if it doesnt exist
User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    place_name = models.CharField(max_length=100, unique=True)
    place_address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.place_name
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.ForeignKey(Place,related_name='events', on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User,related_name='events', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Participation(models.Model):
    event = models.ForeignKey(Event,related_name='participations', on_delete=models.CASCADE)
    content = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='participations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    participation = models.ForeignKey(Participation, related_name='conversationmessages', on_delete=models.CASCADE)
    message = models.TextField()
    created_by = models.ForeignKey(User,related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']