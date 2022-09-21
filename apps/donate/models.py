from django.db import models

from apps.core.models import TimeStampedModel
from apps.donate.validotors import PhoneValidator


class Donate(TimeStampedModel):
    class UserType(models.IntegerChoices):
        Y = (0, "Yuridik shaxs")
        J = (1, "Jismoniy shaxs")

    fio = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=9, validators=[PhoneValidator])
    organization = models.CharField(max_length=60, null=True)
    user_type = models.IntegerField(choices=UserType.choices)
    amount = models.PositiveBigIntegerField()

    def __str__(self):
        return self.fio
