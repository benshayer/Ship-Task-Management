from django.contrib import admin
from .models import TodoList,Category,Announcement

admin.site.register(TodoList)
admin.site.register(Category)
admin.site.register(Announcement)


