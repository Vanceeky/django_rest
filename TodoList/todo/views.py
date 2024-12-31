from django.shortcuts import render
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, views


from .serializers import TodoItemSerializer, ActivityFeedSerializer

# Create your views here.

@api_view(['GET'])
def todo_list(request):
    todo_items = TodoItem.objects.all()

    serializers = TodoItemSerializer(todo_items, many=True).data

    return Response(serializers, status = status.HTTP_200_OK)


@api_view(['POST'])
def add_todo(request):
    data = request.data

    serializers = TodoItemSerializer(data=data)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status = status.HTTP_201_CREATED)
    
    return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo_item = TodoItem.objects.get(pk=pk)

    except TodoItem.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.METHOD == "DELETE":
        todo_item.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    elif request.METHOD == "PUT":
        data = request.data

        serializer = TodoItemSerializer(todo_item, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def activity_feed(request):
    activity_feed = ActivityFeed.objects.all()
    serializer = ActivityFeedSerializer(activity_feed, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class ActivityFeedCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ActivityFeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    