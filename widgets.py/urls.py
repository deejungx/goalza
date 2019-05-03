from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('about/', views.aboutPageView, name='about'),
    path('settings/', views.futsalSettings, name='settings')
]
