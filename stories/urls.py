from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
    path('story/new/', views.story_new, name='story_new'),
    path('story/<int:pk>/edit/', views.story_edit, name='story_edit'),
]
