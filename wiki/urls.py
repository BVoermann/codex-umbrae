from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('<slug:system_slug>/', views.wiki_home, name='wiki_home'),
    path('<slug:system_slug>/list/', views.wiki_list, name='wiki_list'),
    path('<slug:system_slug>/search/', views.wiki_search, name='wiki_search'),
    path('<slug:system_slug>/create/', views.wiki_create, name='wiki_create'),
    path('<slug:system_slug>/type/<str:entry_type>/', views.wiki_by_type, name='wiki_by_type'),
    path('<slug:system_slug>/<slug:entry_slug>/', views.wiki_detail, name='wiki_detail'),
    path('<slug:system_slug>/<slug:entry_slug>/edit/', views.wiki_edit, name='wiki_edit'),
]
