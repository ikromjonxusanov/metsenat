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

    organization = models.CharField(max_length=60, null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=UserType.choices)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.New)
    donate_amount = models.PositiveBigIntegerField()


class DonatesForStudent(TimeStampedModel):
    donater = models.ForeignKey(Donate, on_delete=models.RESTRICT, related_name='donater')
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, related_name='donater_for_student')

    amount = models.PositiveBigIntegerField()

    class Meta:
        unique_together = ['donater', 'student']
