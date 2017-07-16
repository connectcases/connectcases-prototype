from django.contrib import admin
from .models import Device, Patient

class DeviceAdmin(admin.ModelAdmin):
        pass

admin.site.register(Device, DeviceAdmin)

class PatientAdmin(admin.ModelAdmin):
        pass

admin.site.register(Patient, PatientAdmin)
