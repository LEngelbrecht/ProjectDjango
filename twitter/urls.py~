from django.conf.urls import patterns, include, url

from django.contrib import admin
from twitter import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.connection, name='login'),
    url(r'^logout$', views.deconnection, name='logout'),
    url(r'^accueil$', views.user_profil, name='resume'),
    url(r'^tweet$', views.envoyer_tweet, name='tweeter'),	
    url(r'^(?P<username>\w+)/$', views.details, name='profil'),
    url(r'^inscription$', views.create_account, name='inscription'),
)
