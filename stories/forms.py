from django import forms

from .models import Story

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('story_title', 'story_text', 'incident_type', 'perpetrator_type')