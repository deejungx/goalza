from django import forms

class FutsalSettingsForm(forms.Form):

    futsal_name = forms.CharField(widget=forms.TextInput(),
                                  required=True)
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                   attrs={
                                'class': 'time_input',
                                'data-time-format': 'H:i:s'
                                    }),
                                    required=True)
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',
                                   attrs={
                                'class': 'time_input',
                                'data-time-format': 'H:i:s'
                                    }),
                                    required=True)

class NewGroundForm(forms.Form):

    ground_number = forms.IntegerField(widget=forms.NumberInput())
    ground_name = forms.CharField(widget=forms.TextInput())
