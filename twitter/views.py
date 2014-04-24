from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.http import HttpResponse
from twitter.models import User, Tweet
from twitter.forms import InscriptionForm


def create_account(request):
   if request.method == 'POST':
   	inscription_form = InscriptionForm(request.POST)
	if inscription.is_valid():
		user=User()
        	user.name= inscription.cleaned_data['name']
		user.first = inscription.cleaned_data['firstname']
 		user.save()
		return HttpResponse('OK!')
   else:
   	inscription_form = InscriptionForm()
	contexte = {'inscription_form' : inscription_form}
   	return render(request, 'create.html', contexte)

@login_required
def index(request):
   tweet = Tweet.objects.all.order_by('date')
   contexte={'tweet_form' : tweet_form,}
   return render(request, 'bienvenue.html', contexte)

