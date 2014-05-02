from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from twitter.models import UserProfil, Tweet, Abonnement
from twitter.forms import InscriptionForm, TweetForm, LoginForm


def create_account(request):
   if request.method == 'POST':
   	inscription_form = InscriptionForm(request.POST)
	if inscription_form.is_valid():
		user = UserProfil
		user.last_name = inscription_form.cleaned_data["last_name"]
		user.first_name = inscription_form.cleaned_data["first_name"]
		user.username = inscription_form.cleaned_data["username"]
		user.email = inscription_form.cleaned_data["email"]
		user.password = inscription_form.cleaned_data["password"]
		user.Avatar = inscription_form.cleaned_data["Avatar"]
		user.save()
		return render(request, 'bienvenue.html')
   else:
   	inscription_form = InscriptionForm()
	return render(request, 'create.html')

def index(request):
      tweets = Tweet.objects.all().order_by('date')
      contexte = {'tweets' : tweets}
      return render(request,'bienvenue.html', contexte)

def connection(request):
      	login_form = LoginForm()
	contexte = {'login_form' : login_form}
   	return render(request, 'login.html', contexte)

@login_required
def logged_in(request):
	return render_to_response('bienvenue.html',context_instance=RequestContext(request))


