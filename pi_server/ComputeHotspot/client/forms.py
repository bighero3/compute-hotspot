from django import forms


class ComputeForm(forms.Form):
    runtime = forms.IntegerField(label="Requested Runtime (in seconds)")
    file = forms.FileField()
