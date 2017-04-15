"""charades URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from charades.views import index, instructions, select_phrase, acting, guess, \
                           reset, phrase_ready_api, waiting_for_actor, \
                           guess_correct_api

#pylint: disable=invalid-name
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^instructions/$', instructions, name='instructions'),
    url(r'^select_phrase/$', select_phrase, name='select_phrase'),
    url(r'^acting/$', acting, name='acting'),
    url(r'^(\d)/guess/$', guess, name='guess'),
    url(r'^reset/$', reset),
    url(r'^waiting_for_actor/$', waiting_for_actor, name='waiting_for_actor'),

    ### API ###
    url(r'^api/phrase_ready/$', phrase_ready_api, name='phrase_ready'),
    url(r'^api/guess_correct/$',guess_correct_api, name='guess_correct'),
]
