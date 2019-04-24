from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # this tells Django to return the post_list view if you go to the homepage
]