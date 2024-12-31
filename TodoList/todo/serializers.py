from rest_framework import serializers
from .models import TodoItem, ActivityFeed

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem

        fields = '__all__'

class ActivityFeedSerializer(serializers.ModelSerializer):
    class Meta:

        model = ActivityFeed

        fields = '__all__'
