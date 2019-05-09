from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from .decorators import futsal_admin_required
from .forms import FutsalSettingsForm, NewGroundForm, NewPlayer, NewBooking
from .models import FutsalCompany, Ground, Player
import json

decorators = [login_required, futsal_admin_required]

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
            futsal.futsal_name = form.cleaned_data['futsal_name']
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


@method_decorator(decorators, name='dispatch')
class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'


@login_required
@futsal_admin_required
def addNewBooking(request):
    if request.method == 'POST':
        form = NewBooking(request.POST)
        if form.is_valid():
            pass
    else:
        form = NewBooking()
    return render(request, 'pages/add_new_booking.html', {'form': form })


def playerSuggestionModel(request):
    if request.is_ajax():
        phone = request.GET.get('term', '')
        player_qry = Player.objects.filter(phone_number__startswith=phone)
        results = []
        for player in player_qry:
            results.append(player.phone_number)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def playerAutofil(request):
    if request.is_ajax():
        phone = request.GET.get('phone_number', '')
        players = Player.objects.filter(phone_number=phone).values('player_name')
        players_name = list(players)
        data = json.dumps(players_name)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
