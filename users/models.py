from django.db import models
from django.contrib.auth.models import User,Group

class Profile(models.Model):
	departments=[('Electronics','Electronics'),('Machine','Machine'),('Weapon','Weapon'),('Navigation','Navigation'),('Soldier','Soldier')]
	ranks=[('OR-4','Corporal'),('OR-5','Sergeant'),('OR-6','Staff Sergeant'),('OF-1','Lieutenant'),('OF-2','Captain')]
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	department = models.CharField(max_length=100,choices=departments, default='Soldier')
	rank = models.CharField(max_length=100,choices=ranks, default='OR-4')



	def __str__(self):
		return f'{self.user.username} Profile'
