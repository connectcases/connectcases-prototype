from django.forms import ModelForm, ValidationError
from .models import Device

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []

    def clean_upper_colet_from(self):
        if self._missing_upper_teeth() and self.cleaned_data['upper_colet_from'] is None:
            raise ValidationError("This is required when upper teeth are missing")

    def clean_upper_colet_to(self):
        if self._missing_upper_teeth() and self.cleaned_data['upper_colet_to'] is None:
            raise ValidationError("This is required when upper teeth are missing")

    def clean_lower_colet_from(self):
        if self._missing_lower_teeth() and self.cleaned_data['lower_colet_from'] is None:
            raise ValidationError("This is required when lower teeth are missing")

    def clean_lower_colet_to(self):
        if self._missing_lower_teeth() and self.cleaned_data['lower_colet_to'] is None:
            raise ValidationError("This is required when lower teeth are missing")

    def _missing_upper_teeth(self):
        return self.cleaned_data['upper_left_1'] or \
               self.cleaned_data['upper_left_2'] or \
               self.cleaned_data['upper_left_3'] or \
               self.cleaned_data['upper_left_4'] or \
               self.cleaned_data['upper_left_5'] or \
               self.cleaned_data['upper_left_6'] or \
               self.cleaned_data['upper_left_7'] or \
               self.cleaned_data['upper_right_1'] or \
               self.cleaned_data['upper_right_2'] or \
               self.cleaned_data['upper_right_3'] or \
               self.cleaned_data['upper_right_4'] or \
               self.cleaned_data['upper_right_5'] or \
               self.cleaned_data['upper_right_6'] or \
               self.cleaned_data['upper_right_7']

    def _missing_lower_teeth(self):
        return self.cleaned_data['lower_left_1'] or \
               self.cleaned_data['lower_left_2'] or \
               self.cleaned_data['lower_left_3'] or \
               self.cleaned_data['lower_left_4'] or \
               self.cleaned_data['lower_left_5'] or \
               self.cleaned_data['lower_left_6'] or \
               self.cleaned_data['lower_left_7'] or \
               self.cleaned_data['lower_right_1'] or \
               self.cleaned_data['lower_right_2'] or \
               self.cleaned_data['lower_right_3'] or \
               self.cleaned_data['lower_right_4'] or \
               self.cleaned_data['lower_right_5'] or \
               self.cleaned_data['lower_right_6'] or \
               self.cleaned_data['lower_right_7']
