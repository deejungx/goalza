from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django.db import transaction

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_futsal_admin = True
        user.save()
        futsal_admin = Profile.objects.create(user=user)
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
