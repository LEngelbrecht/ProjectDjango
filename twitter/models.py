from django.db import models

class User(models.Model):
        name = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	pseudo = models.CharField(max_length=100)
	email = models.CharField(max_length=200)

class Tweet(models.Model):
      user = models.ForeignKey(User)
      message= models.CharField(max_length=140)
      date = models.DateTimeField('Date published')
