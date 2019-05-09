from django import forms
from .models import Ground, FutsalCompany, Player
from .myFields import DAY_OF_THE_WEEK

class FutsalSettingsForm(forms.Form):

    futsal_name = forms.CharField(widget=forms.TextInput(),
                                  required=True,
                                  max_length=155)
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                   attrs={
                                'class': 'time_input',
                                'data-time-format': 'H:i'
                                    }),
                                    required=True)
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                   attrs={
                                'class': 'time_input',
                                'data-time-format': 'H:i'
                                    }),
                                    required=True)
    def clean(self):
        cleaned_data = super().clean()
        futsalName = cleaned_data.get('futsal_name')
        f = FutsalCompany.objects.filter(futsal_name=futsalName)
        if f.exists():
            raise forms.ValidationError("Futsal with that name already exists. \
                                        Try another")
        return cleaned_data

class NewGroundForm(forms.Form):

    ground_number = forms.IntegerField(widget=forms.NumberInput())
    ground_name = forms.CharField(widget=forms.TextInput())

    def clean(self):
        cleaned_data = super().clean()
        ground_num = cleaned_data.get('ground_number')
        g = Ground.objects.filter(ground_number=ground_num)
        if g.exists():
            raise forms.ValidationError("Ground with given number already \
                                        exists.")
        return cleaned_data

class NewPlayer(forms.Form):

        phone_number = forms.CharField(widget=forms.TextInput())
        player_name = forms.CharField(widget=forms.TextInput())
        player_address = forms.CharField(widget=forms.TextInput(),
                                         required=False,)
        player_email = forms.EmailField(widget=forms.EmailInput(),
                                        required=False,)

        def clean(self):
            cleaned_data = super().clean()
            phoneNum = cleaned_data.get('phone_number')
            playerEmail = cleaned_data.get('player_email')
            p = Player.objects.filter(phone_number=phoneNum)
            q = Player.objects.filter(player_email=playerEmail)
            if p.exists():
                raise forms.ValidationError("Player with given phone number \
                                            already exists.")
            if q.exists():
                raise forms.ValidationError("Player with given Email address\
                                            already exists")
            return cleaned_data


class NewBooking(forms.Form):

    phone_number = forms.CharField(widget=forms.TextInput())
    player_name = forms.CharField(widget=forms.TextInput())
