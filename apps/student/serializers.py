from rest_framework import serializers
from apps.student.models import Student


class AdminStudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['fio', 'phone_number', 'degree_type', 'otm', 'contract_amount']


class AdminStudentListSerializer(serializers.ModelSerializer):
    otm = serializers.CharField(source='otm.name', read_only=True)
    degree_type = serializers.CharField(source='get_degree_type_display')
    # allocated_amount = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Student
        exclude = ['phone_number', 'updated_at']
