from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.models import User
from .models import Category,TodoList, Announcement
from .forms import TaskCreateForm
from django.contrib.auth.decorators import login_required
from users.models import Profile

def home(request):
	context = {
		'tasks' : TodoList.objects.all()
	}
	return render(request,'todo_list/home.html',context)

class AnnouncementsView(ListView):
	model=Announcement
	template_name='todo_list/home.html'
	context_object_name='messages'
	oredering=['-due_date']
	paginate_by = 5

class UserTodoListView(ListView):
	model=TodoList
	template_name='todo_list/user_tasks.html'
	context_object_name='tasks'
	paginate_by = 5

	def get_queryset(self):
		user1 = get_object_or_404(User, username=self.kwargs.get('username'))
		return TodoList.objects.filter(responsibles=user1.profile).order_by('-due_date')

class OfficerTodoListView(ListView):
	model=TodoList
	template_name='todo_list/officer_tasks.html'
	context_object_name='tasks'
	paginate_by = 5

	def get_queryset(self):
		user1 = get_object_or_404(User, username=self.kwargs.get('username'))
		return TodoList.objects.filter(user=user1).order_by('-due_date')


class TodoDetailView(DetailView):
	model=TodoList

@login_required
def create_task(request):
	if request.user.profile.rank.startswith('OF'):
		if request.method=='POST':
			task_form = TaskCreateForm(request.user,request.POST)
			if task_form.is_valid():
				task=task_form.save(commit=False)
				task.user=request.user
				task.save()
				#messages.success(request, f'Your Task has created!')
				return redirect('todo-list-home')
		else:
			task_form = TaskCreateForm(request.user)
			context ={
				'task_form':task_form,
			}
		return render(request, 'todo_list/todolist_form.html',context)
	else:
		return redirect('todo-list-home')

class AnnouncementoCreateView(LoginRequiredMixin,CreateView):
	model=Announcement
	fields=['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		message = self.get_object()
		if self.request.user.profile.rank.startswith('OF'):
			return True
		return False

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
	model=TodoList
	template_name='todo_list/todolist_update.html'
	fields=['title','content','category','due_date']

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		task = self.get_object()
		if self.request.user == task.user:
			return True
		return False
class LowTodoUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
	model=TodoList
	template_name='todo_list/todolist_update.html'
	fields=['content','status']

	def form_valid(self,form):
		form.instance.responsibles.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		task = self.get_object()
		if self.request.user == task.responsibles.user:
			return True
		return False

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
	model=TodoList
	success_url = '/'
	def test_func(self):
		task = self.get_object()
		if self.request.user == task.user:
			return True
		return False

class AnnouncementDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
	model=Announcement
	success_url = '/'
	def test_func(self):
		task = self.get_object()
		if self.request.user == task.author:
			return True
		return False



def about(request):
	return render(request, 'todo_list/about.html')