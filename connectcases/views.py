from django.shortcuts import render

from .forms import DeviceForm

def index(request):
    form = DeviceForm()
    return render(request, 'connectcases/index.html', {'form': form})
