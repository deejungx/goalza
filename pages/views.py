from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .decorators import futsal_admin_required
from .forms import FutsalSettingsForm, NewGroundForm
from .models import FutsalCompany, Ground

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
    # print(futsal)
    if request.method == 'POST':
        form = FutsalSettingsForm(request.POST)
        if form.is_valid():
            futsal.fusal_name = form.cleaned_data['futsal_name']
            futsal.opening_time = form.cleaned_data['opening_time']
            futsal.closing_time = form.cleaned_data['closing_time']
            futsal.save()
            return HttpResponseRedirect('pages/thanks.html')
    else:
        form = FutsalSettingsForm()

    return render(request, 'pages/futsal_settings_page.html', {'form': form, 'futsal': futsal})

@login_required
@futsal_admin_required
def addNewGround(request):
    if request.method == 'POST':
        form = NewGroundForm(request.POST)
        if form.is_valid():
            futsal = request.user.profile.futsal
            groundNum = form.cleaned_data['ground_number']
            groundName = form.cleaned_data['ground_name']
            ground = Ground(ground_number=groundNum, ground_name=groundName, futsalCompany=futsal)
            ground.save()
            return render(request, 'pages/thanks.html')
    else:
        form = NewGroundForm()

    return render(request, 'pages/add_ground_page.html', {'form': form})
