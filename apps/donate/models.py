from django.db import models

from apps.core.models import TimeStampedModel
from apps.donate.validotors import PhoneValidator


class Donate(TimeStampedModel):
    class UserType(models.IntegerChoices):
        Y = (0, "Yuridik shaxs")
        J = (1, "Jismoniy shaxs")

    class Status(models.IntegerChoices):
        New = (0, "Yangi")
        InModeration = (1, "Moderatsiyada")
        Confirmed = (2, "Tasdiqlangxan")
        Canceled = (3, "Bekor qilingan")

    fio = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=9, validators=[PhoneValidator])
    organization = models.CharField(max_length=60, null=True)
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices)
    status = models.PositiveSmallIntegerField(choices=Status.choices)
    donate_amount = models.PositiveBigIntegerField()
    spent_amount = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.fio

    @property
    def amount(self):
        return self.donate_amount - self.spent_amount

    @property
    def is_spend(self):
        return True if self.amount else False
