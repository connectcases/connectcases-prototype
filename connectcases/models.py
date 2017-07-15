from django.db import models

COLET_FROM = [
    ('L1', 'LEFT 1'),
    ('L2', 'LEFT 2'),
    ('L3', 'LEFT 3'),
    ('L4', 'LEFT 4'),
    ('L5', 'LEFT 5'),
    ('L6', 'LEFT 6'),
    ('L7', 'LEFT 7'),
]

COLET_TO = [
    ('R1', 'RIGHT 1'),
    ('R2', 'RIGHT 2'),
    ('R3', 'RIGHT 3'),
    ('R4', 'RIGHT 4'),
    ('R5', 'RIGHT 5'),
    ('R6', 'RIGHT 6'),
    ('R7', 'RIGHT 7'),
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
        max_length=2,
        choices=COLET_FROM,
    )

    upper_colet_to = models.CharField(
        max_length=2,
        choices=COLET_TO,
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
        max_length=2,
        choices=COLET_FROM,
    )

    lower_colet_to = models.CharField(
        max_length=2,
        choices=COLET_TO,
    )

    patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
    )

class Patient(models.Model):
    name = models.CharField(max_length=200)
