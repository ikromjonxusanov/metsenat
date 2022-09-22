from rest_framework import serializers
from apps.student.models import Student


class AdminStudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['fio', 'phone_number', 'degree_type', 'otm', 'contract_amount']
