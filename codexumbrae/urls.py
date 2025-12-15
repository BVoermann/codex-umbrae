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
    path('dnd/', dnd_views.home, name='dnd_home'),
    path('daggerheart/', daggerheart_views.home, name='daggerheart_home'),
]
