from django.contrib import admin
from .models import TodoList,Category,Announcement, Comment, Department

admin.site.register(TodoList)
admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(Department)
@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
	list_display = ('task', 'authour', 'text', 'created', 'active')
	list_filter = ('active','created')
	search_fields = ('name', 'email', 'body')
	actions = ['approve_comments']

	def approve_comments(self, request, queryset):
		queryset.update(active=True)


