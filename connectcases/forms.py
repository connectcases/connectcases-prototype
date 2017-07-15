from django.forms import ModelForm, ValidationError
from .models import Device

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []

    def clean_upper_colet_from(self):
        if self._missing_upper_teeth(self.cleaned_data) and self.cleaned_data['upper_colet_from'] is None:
            raise ValidationError("This is required when upper teeth are missing")

    def clean_upper_colet_to(self):
        if self._missing_upper_teeth(self.cleaned_data) and self.cleaned_data['upper_colet_to'] is None:
            raise ValidationError("This is required when upper teeth are missing")

    def clean_lower_colet_from(self):
        if self._missing_lower_teeth(self.cleaned_data) and self.cleaned_data['lower_colet_from'] is None:
            raise ValidationError("This is required when lower teeth are missing")

    def clean_lower_colet_to(self):
        if self._missing_lower_teeth(self.cleaned_data) and self.cleaned_data['lower_colet_to'] is None:
            raise ValidationError("This is required when lower teeth are missing")

    def clean(self):
        cleaned_data = super(DeviceForm, self).clean()

        upper = self._missing_upper_teeth(cleaned_data)
        lower = self._missing_lower_teeth(cleaned_data)

        if not upper and not lower:
            raise ValidationError("Please select at least one tooth")

    def _missing_upper_teeth(self, cleaned_data):
        return cleaned_data['upper_left_1'] or \
               cleaned_data['upper_left_2'] or \
               cleaned_data['upper_left_3'] or \
               cleaned_data['upper_left_4'] or \
               cleaned_data['upper_left_5'] or \
               cleaned_data['upper_left_6'] or \
               cleaned_data['upper_left_7'] or \
               cleaned_data['upper_right_1'] or \
               cleaned_data['upper_right_2'] or \
               cleaned_data['upper_right_3'] or \
               cleaned_data['upper_right_4'] or \
               cleaned_data['upper_right_5'] or \
               cleaned_data['upper_right_6'] or \
               cleaned_data['upper_right_7']

    def _missing_lower_teeth(self, cleaned_data):
        return cleaned_data['lower_left_1'] or \
               cleaned_data['lower_left_2'] or \
               cleaned_data['lower_left_3'] or \
               cleaned_data['lower_left_4'] or \
               cleaned_data['lower_left_5'] or \
               cleaned_data['lower_left_6'] or \
               cleaned_data['lower_left_7'] or \
               cleaned_data['lower_right_1'] or \
               cleaned_data['lower_right_2'] or \
               cleaned_data['lower_right_3'] or \
               cleaned_data['lower_right_4'] or \
               cleaned_data['lower_right_5'] or \
               cleaned_data['lower_right_6'] or \
               cleaned_data['lower_right_7']
