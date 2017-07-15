from django.forms import ModelForm, ValidationError
from .models import Device

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = []

    def clean_upper_colet_from(self):
        data = self.cleaned_data['upper_colet_from']

        missing_upper = self._missing_upper_teeth(self.cleaned_data)

        if missing_upper and data is None:
            raise ValidationError("This is required when upper teeth are missing")

        if not missing_upper and data is not None:
            raise ValidationError("This is not required when no upper teeth are missing")

        return data

    def clean_upper_colet_to(self):
        data = self.cleaned_data['upper_colet_to']

        missing_upper = self._missing_upper_teeth(self.cleaned_data)

        if missing_upper and data is None:
            raise ValidationError("This is required when upper teeth are missing")

        if not missing_upper and data is not None:
            raise ValidationError("This is not required when no upper teeth are missing")

        return data

    def clean_lower_colet_from(self):
        data = self.cleaned_data['lower_colet_from']

        missing_lower = self._missing_lower_teeth(self.cleaned_data)

        if missing_lower and data is None:
            raise ValidationError("This is required when lower teeth are missing")

        if not missing_lower and data is not None:
            raise ValidationError("This is not required when no lower teeth are missing")

        return data

    def clean_lower_colet_to(self):
        data = self.cleaned_data['lower_colet_to']

        missing_lower = self._missing_lower_teeth(self.cleaned_data)

        if missing_lower and data is None:
            raise ValidationError("This is required when lower teeth are missing")

        if not missing_lower and data is not None:
            raise ValidationError("This is not required when no lower teeth are missing")
 
        return data

    def clean(self):
        cleaned_data = super(DeviceForm, self).clean()

        upper = self._missing_upper_teeth(cleaned_data)
        lower = self._missing_lower_teeth(cleaned_data)

        if not upper and not lower:
            raise ValidationError("Please select at least one tooth")

        return cleaned_data

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
