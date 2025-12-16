"""
URL configuration for codexumbrae project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from vampire import views as vampire_views
from kult import views as kult_views
from dnd import views as dnd_views
from daggerheart import views as daggerheart_views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('vampire/', vampire_views.home, name='vampire_home'),
    path('kult/', kult_views.home, name='kult_home'),
    path('dnd/home/', dnd_views.home, name='dnd_home'),
    path('daggerheart/', daggerheart_views.home, name='daggerheart_home'),
    path('dnd/campaign/', dnd_views.campaign, name='dnd_campaign'),
    path('dnd/sessions', dnd_views.sessions, name='dnd_sessions'),
    path('dnd/lore/', dnd_views.lore, name='dnd_lore'),
    path('dnd/characters', dnd_views.characters, name='dnd_characters'),
    path('dnd/media/', dnd_views.media, name='dnd_media'),
    path('dnd/search/', dnd_views.search, name='dnd_search'),
]
