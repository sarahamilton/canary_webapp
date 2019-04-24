from django.shortcuts import render

# A view is a function that returns something -- in this case HTML
def post_list(request):
    return render(request, 'blog/post_list.html', {})