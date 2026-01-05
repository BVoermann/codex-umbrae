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
from . import auth_views
from vampire import views as vampire_views
from kult import views as kult_views
from dnd import views as dnd_views
from daggerheart import views as daggerheart_views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    # Sessions password protection URLs
    path('dnd/sessions/login', lambda request: auth_views.sessions_password_check(request, 'dnd'), name='dnd_sessions_login'),
    path('vampire/sessions/login', lambda request: auth_views.sessions_password_check(request, 'vampire'), name='vampire_sessions_login'),
    path('kult/sessions/login', lambda request: auth_views.sessions_password_check(request, 'kult'), name='kult_sessions_login'),
    path('daggerheart/sessions/login', lambda request: auth_views.sessions_password_check(request, 'daggerheart'), name='daggerheart_sessions_login'),

    path('vampire/', vampire_views.home, name='vampire_home'),
    path('kult/', kult_views.home, name='kult_home'),
    path('dnd/home/', dnd_views.home, name='dnd_home'),
    path('daggerheart/home/', daggerheart_views.home, name='daggerheart_home'),
    path('dnd/campaign/', dnd_views.campaign, name='dnd_campaign'),
    path('dnd/sessions', dnd_views.sessions, name='dnd_sessions'),
    path('dnd/lore/', dnd_views.lore, name='dnd_lore'),
    path('dnd/characters', dnd_views.characters, name='dnd_characters'),
    path('dnd/media/', dnd_views.media, name='dnd_media'),
    path('dnd/search/', dnd_views.search, name='dnd_search'),
    path('daggerheart/campaign/', daggerheart_views.campaign, name='daggerheart_campaign'),
    path('daggerheart/sessions', daggerheart_views.sessions, name='daggerheart_sessions'),
    path('daggerheart/lore/', daggerheart_views.lore, name='daggerheart_lore'),
    path('daggerheart/characters', daggerheart_views.characters, name='daggerheart_characters'),
    path('daggerheart/media/', daggerheart_views.media, name='daggerheart_media'),
    path('daggerheart/search/', daggerheart_views.search, name='daggerheart_search'),
    path('kult/campaign/', kult_views.campaign, name='kult_campaign'),
    path('kult/sessions', kult_views.sessions, name='kult_sessions'),
    path('kult/lore/', kult_views.lore, name='kult_lore'),
    path('kult/characters', kult_views.characters, name='kult_characters'),
    path('kult/media/', kult_views.media, name='kult_media'),
    path('kult/search/', kult_views.search, name='kult_search'),
    path('vampire/campaign/', vampire_views.campaign, name='vampire_campaign'),
    path('vampire/sessions', vampire_views.sessions, name='vampire_sessions'),
    path('vampire/lore/', vampire_views.lore, name='vampire_lore'),
    path('vampire/characters', vampire_views.characters, name='vampire_characters'),
    path('vampire/media/', vampire_views.media, name='vampire_media'),
    path('vampire/search/', vampire_views.search, name='vampire_search'),
]
