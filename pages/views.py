from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .decorators import futsal_admin_required
from .forms import FutsalSettingsForm, NewGroundForm, NewPlayer
from .models import FutsalCompany, Ground, Player

def homePageView(request):
    return render(request, 'pages/home.html')

@login_required
@futsal_admin_required
def aboutPageView(request):
    return render(request, 'pages/about.html')


@login_required
@futsal_admin_required
def futsalSettings(request):
    futsal = request.user.profile.futsal
    if request.method == 'POST':
        form = FutsalSettingsForm(request.POST)
        if form.is_valid():
            futsal.fusal_name = form.cleaned_data['futsal_name']
            futsal.opening_time = form.cleaned_data['opening_time']
            futsal.closing_time = form.cleaned_data['closing_time']
            futsal.save()
    else:
        form = FutsalSettingsForm()

    return render(request, 'pages/futsal_settings_page.html', {'form': form,
                  'futsal': futsal})

@login_required
@futsal_admin_required
def addNewGround(request):
    grounds = request.user.profile.futsal.ground_set.all()
    if request.method == 'POST':
        form = NewGroundForm(request.POST)
        if form.is_valid():
            futsal = request.user.profile.futsal
            groundNum = form.cleaned_data['ground_number']
            groundName = form.cleaned_data['ground_name']
            ground = Ground(ground_number=groundNum,
                            ground_name=groundName,
                            futsalCompany=futsal)
            ground.save()
    else:
        form = NewGroundForm()

    return render(request, 'pages/ground_settings_page.html', {'form': form,
                  'grounds':grounds})


@login_required
@futsal_admin_required
def addNewPlayer(request):
    if request.method == 'POST':
        form = NewPlayer(request.POST)
        if form.is_valid():
            phoneNum = form.cleaned_data['phone_number']
            playerName = form.cleaned_data['player_name']
            if form.cleaned_data['player_address']:
                playerAddress = form.cleaned_data['player_address']
            else:
                playerAddress = None
            if form.cleaned_data['player_email']:
                playerEmail = form.cleaned_data['player_email']
            else:
                playerEmail = None
            player = Player(phone_number=phoneNum,
                            player_name=playerName,
                            player_address=playerAddress,
                            player_email=playerEmail,
                            )
            player.save()
    else:
        form = NewPlayer()

    return render(request, 'pages/add_new_player_page.html', {'form': form })
