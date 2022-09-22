from django.db import models

from apps.core.models import TimeStampedModel, Person
from apps.student.models import Student


class Donate(Person):
    class UserType(models.IntegerChoices):
        Y = (0, "Yuridik shaxs")
        J = (1, "Jismoniy shaxs")

    class Status(models.IntegerChoices):
        New = (0, "Yangi")
        InModeration = (1, "Moderatsiyada")
        Confirmed = (2, "Tasdiqlangxan")
        Canceled = (3, "Bekor qilingan")

    organization = models.CharField(max_length=60, null=True)
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.New)
    donate_amount = models.PositiveBigIntegerField()
    spent_amount = models.PositiveBigIntegerField(default=0)

    @property
    def amount(self):
        return self.donate_amount - self.spent_amount

    @property
    def is_spend(self):
        return True if self.amount else False


class DonatesForStudent(TimeStampedModel):
    donater = models.ForeignKey(Donate, on_delete=models.RESTRICT, related_name='donater')
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, related_name='donater_for_student')

    amount = models.PositiveBigIntegerField()
