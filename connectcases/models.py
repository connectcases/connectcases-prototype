from django.db import models

def generate_choices(jaw, side):
    l = []
    for tooth in range(1, 8):
        l.append(
            (
                '{}_{}_{}'.format(jaw, side, tooth),
                '{} {}'.format(side.upper(), tooth),
            )
        )
    return l

TEETH_CHOICES = [
    ('01', 'Standard'),
    ('02', 'High Quality'),
]

BASEPLATE_CHOICES = [
    ('AC', 'Acrylic'),
    ('HI', 'High Impact Acrylic'),
]

class Device(models.Model):
    upper_left_1 = models.BooleanField(default=False)
    upper_left_2 = models.BooleanField(default=False)
    upper_left_3 = models.BooleanField(default=False)
    upper_left_4 = models.BooleanField(default=False)
    upper_left_5 = models.BooleanField(default=False)
    upper_left_6 = models.BooleanField(default=False)
    upper_left_7 = models.BooleanField(default=False)

    upper_right_1 = models.BooleanField(default=False)
    upper_right_2 = models.BooleanField(default=False)
    upper_right_3 = models.BooleanField(default=False)
    upper_right_4 = models.BooleanField(default=False)
    upper_right_5 = models.BooleanField(default=False)
    upper_right_6 = models.BooleanField(default=False)
    upper_right_7 = models.BooleanField(default=False)

    upper_colet_from = models.CharField(
        max_length=13,
        choices=generate_choices('upper', 'right'),
        null=True,
        blank=True,
    )

    upper_colet_to = models.CharField(
        max_length=13,
        choices=generate_choices('upper', 'left'),
        null=True,
        blank=True,
    )

    lower_left_1 = models.BooleanField(default=False)
    lower_left_2 = models.BooleanField(default=False)
    lower_left_3 = models.BooleanField(default=False)
    lower_left_4 = models.BooleanField(default=False)
    lower_left_5 = models.BooleanField(default=False)
    lower_left_6 = models.BooleanField(default=False)
    lower_left_7 = models.BooleanField(default=False)

    lower_right_1 = models.BooleanField(default=False)
    lower_right_2 = models.BooleanField(default=False)
    lower_right_3 = models.BooleanField(default=False)
    lower_right_4 = models.BooleanField(default=False)
    lower_right_5 = models.BooleanField(default=False)
    lower_right_6 = models.BooleanField(default=False)
    lower_right_7 = models.BooleanField(default=False)

    lower_colet_from = models.CharField(
        max_length=13,
        choices=generate_choices('lower', 'right'),
        null=True,
        blank=True,
    )

    lower_colet_to = models.CharField(
        max_length=13,
        choices=generate_choices('lower', 'left'),
        null=True,
        blank=True,
    )

    patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    photo = models.ImageField(blank=True, null=True)

    teeth = models.CharField(
        max_length=2,
        choices=TEETH_CHOICES,
        default='01',
    )

    baseplate = models.CharField(
        max_length=2,
        choices=BASEPLATE_CHOICES,
        default='AC',
    )

    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return '({}) Device for {}'.format(self.id, self.patient.name)

class Patient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
