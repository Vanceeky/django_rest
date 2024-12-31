from . import views

from django.urls import path
from .views import ActivityFeedCreateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo'

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('add-todo/',views.add_todo, name="add_todo"),
    path('todo/detail/<int:pk>/', views.todo_detail, name="todo_detial"),

    path('activity-feed/', ActivityFeedCreateView.as_view(), name='activity-feed-create'),
    path('activity-feed-list/', views.activity_feed, name='activity-feed-list'),
]


