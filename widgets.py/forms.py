from django import forms

class FutsalSettingsForm(forms.Form):

    futsal_name = forms.CharField(widget=forms.TextInput())
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                   attrs={
                                'class': 'time_input',
                                'data-time-format': 'H:i:s'
                                    }))
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                   attrs={
                                'class': 'time_input',
                                'data-time-format': 'H:i:s'
                                    }))
