from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('about/', views.aboutPageView, name='about'),
    path('settings/', views.futsalSettings, name='settings'),
    path('settings/add_ground/', views.addNewGround, name='addground'),
    path('settings/add_player/', views.addNewPlayer, name='addplayer'),
]
