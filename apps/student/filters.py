from django_filters.rest_framework import FilterSet, filters

from apps.student.models import Student


class AdminStudentFilter(FilterSet):
    degree_type = filters.ChoiceFilter(field_name='degree_type', choices=(
        ("Bakalavr", "Bakalavr"),
        ("Magistr", "Magistr")
    ))

    class Meta:
        model = Student
        fields = ['otm']
