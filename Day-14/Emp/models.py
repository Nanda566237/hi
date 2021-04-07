from django.db import models

# Create your models here.
 
class UsrRg(models.Model):
	username= models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	age = models.IntegerField(max_length=120)
	def __str__(self):
		return self.username+" "+self.email



class NewData(models.Model):
	ch=[('M','male'),('F','female')]
	mobile=models.IntegerField(default=9576847535)
	gender=models.CharField(max_length=10,choices=ch)
	pid=models.OneToOneField(UsrRg,on_delete=models.CASCADE)
