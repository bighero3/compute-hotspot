from django.forms.fields import ComboField
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ComputeForm
from . import handlers


def index(request):
    if request.method == 'GET':
        form = ComputeForm()
        return render(request, "client/index.html", {'form': form})
    elif request.method == 'POST':
        form = ComputeForm(request.POST, request.FILES)
        if form.is_valid():
            filepath = handlers.handle_uploaded_file(
                request.FILES['file'])
            context = {
                'memory': request.POST['memory'],
                'runtime': request.POST['runtime']
            }
            handlers.copy_file_to_remote_machine(
                filepath, "~/files/.", "vinczeza@teach.cs.utoronto.ca")
            return render(request, 'client/compute.html', context)
        else:
            return HttpResponse("Invalid form entry.")
