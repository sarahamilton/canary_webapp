from django.conf import settings
from django.db import models
from django.utils import timezone


class Story(models.Model):
    '''
    Story model to hold all attributes of a story. When we have settled on this we can change it.
    For now, here are a few basics.
    Eventually, will need to add enums for the different choices 
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story_title = models.CharField(max_length=200)
    story_text = models.TextField()
    incident_type = models.TextField()
    perpetrator_type = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.story_title
