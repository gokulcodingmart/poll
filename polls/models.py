from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Polllist(models.Model):	
	title = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)



class Choice(models.Model):	
    votes = models.IntegerField(default=0)
    option = models.TextField()
    poll = models.ForeignKey(Polllist, on_delete=models.CASCADE)
    
class Vote(models.Model):	
	email = models.CharField(null=True, max_length=100)
	option = models.ManyToManyField(Choice)