from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Story
from .forms import StoryForm

def story_list(request):
    stories = Story.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stories/story_list.html', {'stories': stories})

def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'stories/story_detail.html', {'story': story})

def story_new(request):
    '''
    This method lets us either submit a form and redirects to the details page, or gives us the blank form.
    '''
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.published_date = timezone.now()
            story.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm()
    return render(request, 'stories/story_edit.html', {'form': form})

def story_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.published_date = timezone.now()
            story.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm(instance=story)
    return render(request, 'stories/story_edit.html', {'form': form})
