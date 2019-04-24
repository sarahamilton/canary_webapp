from django.shortcuts import render
from django.utils import timezone
from .models import Post

# A view is a function that returns something -- in this case HTML
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) # everything from user, view, params
    