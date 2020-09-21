from django import forms
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import TodoList, Comment
from users.models import Profile

class TaskCreateForm(forms.ModelForm):
	model=TodoList
	class Meta:
		model=TodoList
		fields=['title','content','category','due_date','responsibles']
	def __init__(self,user,*args,**kwargs):
		super(TaskCreateForm,self).__init__(*args,**kwargs)
		division=Profile.objects.filter(user=user)[0].division
		self.fields['responsibles'].queryset=Profile.objects.filter(division=division)

class OfficerTaskUpdateForm(forms.ModelForm):
	model=TodoList
	class Meta:
		model=TodoList
		fields=['title','content','category','due_date','responsibles']
	def __init__(self,user,*args,**kwargs):
		super(TaskCreateForm,self).__init__(*args,**kwargs)
		division=Profile.objects.filter(user=user)[0].division
		self.fields['responsibles'].queryset=Profile.objects.filter(division=division)

class SoldierTaskUpdateForm(forms.ModelForm):
	model=TodoList
	class Meta:
		model=TodoList
		fields=['status']
	def __init__(self,user,*args,**kwargs):
		super(TaskCreateForm,self).__init__(*args,**kwargs)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields= ['text']
