from .models import *
from django import forms
from django.forms import ModelForm, TextInput,FileInput

class locationForm(forms.ModelForm):
    class Meta:
        model = location
        fields = ('area',)

class ip_addressForm(forms.ModelForm):
    class Meta:
        model = ip_address
        fields = ('area', 'ip', 'port', 'strs')

class live_track_recordForm(forms.ModelForm):
    class Meta:
        model = live_track_record
        fields = ('name', 'area', 'ip')
