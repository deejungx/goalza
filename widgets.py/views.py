from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from .decorators import futsal_admin_required
from .forms import FutsalSettingsForm
from .models import FutsalCompany

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
            return render(request, 'pages/thanks.html')
    else:
        form = FutsalSettingsForm()

    return render(request, 'pages/futsal_settings_page.html', {'form': form, 'futsal': futsal})
