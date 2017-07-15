from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import DeviceForm

class Index(View):
    def get(self, request):
        form = DeviceForm()
        return render(request, 'connectcases/index.html', {'form': form})

    def post(self, request):
        form = DeviceForm(request.POST)

        if form.is_valid():
            device = form.save()
            return redirect('device-created', device_id=device.id)
        else:
            return render(request, 'connectcases/index.html', {'form': form})

class DeviceCreated(View):
    def get(self, request, device_id):
        return render(request, 'connectcases/created.html', {'device_id': device_id})

