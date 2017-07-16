from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView

from .models import Device, TEETH_CHOICES, BASEPLATE_CHOICES
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

    def get(self, request):
        teeth_choices = dict(TEETH_CHOICES)
        bp_choices = dict(BASEPLATE_CHOICES)
        devices = Device.objects.order_by('id')
        for dev in devices:
            dev.teeth = teeth_choices.get(dev.teeth)
            dev.baseplate = bp_choices.get(dev.baseplate)
        ctx = { 'devices': devices }
        return render(request, 'connectcases/device_list.html', ctx)
