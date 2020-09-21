from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import users.models
from django.contrib.auth import get_user_model

#from project_todo_list.todo_list_app.users.models import Profile

class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be shown when called

class Department(models.Model): # The Department table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")
    def __str__(self):
        return self.name #name to be shown when called


class Announcement(models.Model): 
    title=models.CharField(max_length=250)
    content=models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Announcement")
        verbose_name_plural = ("Announcements")
    def __str__(self):
        return self.title #name to be shown when called
    def get_absolute_url(self):
        return reverse('todo-list-home')

class TodoList(models.Model): #Todolist able name that inherits models.Model
    statuses=[('Not Seen Yet','Not Seen Yet'),('Working on it','Working on it'),('Done','Done'),('Stuck','Stuck')]
    user1=get_user_model().username
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, default="general",on_delete=models.CASCADE) # a foreignkey
    status = models.CharField(max_length=100,choices=statuses,default='Not Seen Yet')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    responsibles=models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name="responsible")
    deadline=models.BooleanField(default=False)



    def __str__(self): 
    	return self.title #name to be shown when called

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})


class Comment(models.Model): # The Category table name that inherits models.Model
    task = models.ForeignKey(TodoList,on_delete=models.CASCADE, related_name='comments')
    authour=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(blank=True)
    created= models.DateTimeField(default=timezone.now)
    active=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment= True
        self.save()

    def __str__(self):
        return self.text #name to be shown when called
