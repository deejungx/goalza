from django.urls import path
from .views import PlayerListView
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('about/', views.aboutPageView, name='about'),
    path('settings/', views.futsalSettings, name='settings'),
    path('settings/add_ground/', views.addNewGround, name='addground'),
    path('settings/add_player/', views.addNewPlayer, name='addplayer'),
    path('settings/player_list/', PlayerListView.as_view(), name='player-list'),
    path('settings/new_booking/', views.addNewBooking, name='addBooking'),
    path('ajax_calls/player_contact/', views.playerSuggestionModel, name='playerSuggestion'),
    path('ajax_calls/player_autofil/', views.playerAutofil, name='playerAutofil'),
]
