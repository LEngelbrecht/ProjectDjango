from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from twitter.models import UserProfil, Tweet, Abonnement
from twitter.forms import InscriptionForm, TweetForm, LoginForm

def create_account(request):
   if request.method == 'POST':
   	inscription_form = InscriptionForm(request.POST)
	if inscription_form.is_valid():
		user = UserProfil()
		user.last_name = inscription_form.cleaned_data["last_name"]
		user.first_name = inscription_form.cleaned_data["first_name"]
		user.username = inscription_form.cleaned_data["username"]
		user.email = inscription_form.cleaned_data["email"]
		user.set_password(inscription_form.cleaned_data["password"])
		user.Avatar = inscription_form.cleaned_data["Avatar"]
		user.save()
		Login(request)
		contexte = {'user' : user}
		return render(request, 'bienvenue.html', user)
   else:
   	inscription_form = InscriptionForm()
   contexte = {'inscription_form' : inscription_form}
   return render(request, 'create.html', contexte)

@login_required(login_url = '/login')
def user_profil(request, username, abo= False):
	if request.user.is_authenticated():
	      login = UserProfil.object(pk = request.user.pk)	
	      user = get_object_or_404(UserProfil, username= username)
	      if login != user or abo == False:
			abonnement = Abonnement.objects.filter(suiveur = user).filter(suivi = login)
	      		tweets = Tweet.objects.all().order_by('date')
	      else:
			abonnement = []
			suiveur = Abonnement.objects.filter(suivi = login)
			tweets = []
			for i in suiveur:
				tweets += Tweet.objects.filter(i.suiveur)
			tweets.sort(key = lambda x : x.date, reverse= True)
	      nombre_tweet = Tweet.object.filter(user = user).count()-1
              nombre_abonnee = Abonnement.object.filter(suiveur = user).count()-1
 	      nombre_abonnement = Abonnement.object.filter(suivi = user).count()-1
	      contexte = {'login' : login, 'user' : user,  'nombre_tweet' : nombre_tweet, 'nombre_abonnee' : nombre_abonnee, 'nombre_abonnement' : nombre_abonnement,}
	      return render(request,'bienvenue.html', contexte)

	return index(request)
def index(request):
	if request.user.is_authenticated():
		user = request.user
	else:
		user = UserProfil()
	return user_profil(request, user.username, True)

def connection(request):
    if request.method == 'POST':
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			login(request, user)
			contexte = {'user' : user,}
			return render(request, 'bienvenue.html', contexte)
		else:
			login_form = LoginForm()
	else:
		login_form = LoginForm()
    else:
	login_form = LoginForm()

    contexte = {'login_form' : login_form}
    return render(request, 'login.html', contexte)

def deconnection(request):
	if request.user.is_authenticated():
		logout(request)
	return index(request)


