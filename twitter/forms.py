from django import forms
from twitter.models import User

class InscriptionForm (forms.ModelForm):
      class Meta:
    	model = User
        fields  = ['name', 'firstname' , 'pseudo', 'email']
