from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView

from .models import Device
from .forms import DeviceForm

class IndexView(View):
    def get(self, request, device_id=None):
        return render(request, 'connectcases/index.html')

class DeviceView(View):
    def get(self, request, device_id=None):
        if device_id:
            device = get_object_or_404(Device, id=device_id)
            form = DeviceForm(instance=device)
        else:
            form = DeviceForm()

        return render(request, 'connectcases/device.html', {'form': form})

    def post(self, request, device_id=None):
        if device_id:
            device = get_object_or_404(Device, id=device_id)
            form = DeviceForm(request.POST, request.FILES, instance=device)
        else:
            form = DeviceForm(request.POST, request.FILES)

        if form.is_valid():
            device = form.save()
            return redirect('device', device_id=device.id)
        else:
            return render(request, 'connectcases/device.html', {'form': form})

class DeviceListView(ListView):
    model = Device
