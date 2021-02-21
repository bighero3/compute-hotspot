from django import forms
from django.forms.widgets import NumberInput, RadioSelect


class RangeInput(NumberInput):
    input_type = 'range'


class ComputeForm(forms.Form):
    runtime = forms.IntegerField(
        label="", widget=RangeInput(attrs={'min': "1", "max": "100", "onchange": "updateTextInput(this.value);", "value": "1"}))
    file = forms.FileField(label="", widget=forms.FileInput(
        attrs={'class': 'file-input'}))
