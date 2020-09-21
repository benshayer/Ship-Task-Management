from django.db import models
from todo_list.models import Department
from django.contrib.auth.models import User,Group

class Profile(models.Model):
	#departments=[('Electronics','Electronics'),('Machine','Machine'),('Weapon','Weapon'),('Navigation','Navigation'),('Soldier','Soldier')]
	ranks=[('Employee','Employee'),('Manager','Manager')]
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	#department = models.CharField(max_length=100,choices=departments, default=1)
	division=models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
	rank = models.CharField(max_length=100,choices=ranks, default='Employee')



	def __str__(self):
		return f'{self.user.username} Profile'
