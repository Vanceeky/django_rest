from django.contrib import admin
from . models import TodoItem, ActivityFeed

# Register your models here.


admin.site.register(TodoItem)
admin.site.register(ActivityFeed)