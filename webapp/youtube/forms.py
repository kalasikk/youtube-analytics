from django import forms

class IdForm(forms.Form):
    channel_id = forms.CharField(label='Your channel ID', max_length=50)