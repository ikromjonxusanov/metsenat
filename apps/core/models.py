from django.db import models

from django.core.validators import MinValueValidator

from apps.core.validators import PhoneValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):
    fio = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=9, validators=[PhoneValidator()])

    def __str__(self):
        return self.fio

    class Meta:
        abstract = True


class OTM(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
