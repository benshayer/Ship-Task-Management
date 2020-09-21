from django.urls import path
from .views import AnnouncementsView,TodoUpdateView,TodoDeleteView,UserTodoListView,LowTodoUpdateView,OfficerTodoListView,AnnouncementoCreateView,AnnouncementDeleteView
from . import views
urlpatterns = [
    path('', AnnouncementsView.as_view(), name='todo-list-home'),
    path('user/<str:username>/', UserTodoListView.as_view(), name='user-tasks'),
    path('user/<str:username>/officer/', OfficerTodoListView.as_view(), name='officer-tasks'),
    path('todo_list/<int:pk>/', views.task_detail, name='task-detail'),
    path('todo_list/<int:pk>/update/', TodoUpdateView.as_view(), name='task-update'),
    path('todo_list/<int:pk>/updatelow/', LowTodoUpdateView.as_view(), name='task-update-low'),
    path('todo_list/<int:pk>/delete/', TodoDeleteView.as_view(), name='task-delete'),
    path('message/<int:pk>/delete/', AnnouncementDeleteView.as_view(), name='message-delete'),
    path('todo_list/new/', views.create_task, name='task-create'),
    path('todo_list/new_message/', AnnouncementoCreateView.as_view(), name='message-create'),
    path('about/', views.about, name='todo-list-about'),
]
