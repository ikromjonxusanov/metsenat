from django.db import models

from apps.core.models import Person, OTM


class Student(Person):
    class DegreeType(models.TextChoices):
        bachelor = ("Bakalavr", "Bakalavr")
        master = ("Magistr", "Magistr")

    degree_type = models.CharField(max_length=20, choices=DegreeType.choices)
    otm = models.ForeignKey(OTM, on_delete=models.RESTRICT)
    contract_amount = models.PositiveBigIntegerField()

    def __str__(self):
        return self.fio
