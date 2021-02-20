from django import forms


class ComputeForm(forms.Form):
    memory = forms.IntegerField(label="Requested Memory (bytes)")
    runtime = forms.IntegerField(label="Requested Runtime (ms)")
    file = forms.FileField()
