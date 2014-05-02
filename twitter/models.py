from django.db import models
from django.contrib.auth.models import User

#Ajout d'une photo au profil de l'Utilisateur
class UserProfil(User):
      Avatar = models.ImageField(upload_to = "Images/")
       

# Gestion des Tweets
class Tweet(models.Model):
      user = models.ForeignKey(UserProfil)
      message= models.CharField(max_length=140)
      date = models.DateTimeField('Date published')

# Gestion des Abonnements
class Abonnement(models.Model):
	suiveur = models.ForeignKey(UserProfil, related_name = "suiveur")
	suivi = models.ForeignKey(UserProfil, related_name = "suivi")
