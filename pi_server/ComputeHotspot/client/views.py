from django.forms.fields import ComboField
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ComputeForm
from . import handlers
import uuid


def index(request):
    if request.method == 'GET':
        form = ComputeForm()
        return render(request, "client/index.html", {'form': form})
    elif request.method == 'POST':
        form = ComputeForm(request.POST, request.FILES)
        if form.is_valid():
            filepath = handlers.handle_uploaded_file(
                request.FILES['file'])
            handlers.copy_file_to_remote_machine(
                filepath, "~/files/.", "pi_01@52.142.54.92")
            result = handlers.execute_file_on_remote_machine(
                filepath, request.POST['runtime'], "pi_01", "52.142.54.92")
            context = {
                'runtime': request.POST['runtime'],
                'result': result
            }
            return render(request, 'client/compute.html', context)
        else:
            return HttpResponse("Invalid form entry.")
