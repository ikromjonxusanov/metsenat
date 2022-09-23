from rest_framework import serializers

from apps.core.helpers import parse_phone_number
from apps.donate.serializers.admin import StudentDonaterListSerializer
from apps.student.models import Student


class AdminStudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['fio', 'phone_number', 'degree_type', 'otm', 'contract_amount']


class AdminStudentListSerializer(serializers.ModelSerializer):
    otm = serializers.CharField(source='otm.name', read_only=True)
    degree_type = serializers.CharField(source='get_degree_type_display')
    allocated_amount = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Student
        exclude = ['phone_number', 'updated_at']


class AdminStudentRetrieveSerializer(serializers.ModelSerializer):
    otm = serializers.CharField(source='otm.name', read_only=True)
    degree_type = serializers.CharField(source='get_degree_type_display')
    allocated_amount = serializers.IntegerField(read_only=True, default=0)
    phone_number = serializers.SerializerMethodField()
    donaters = StudentDonaterListSerializer(source="donater_for_student", many=True, read_only=True)

    @staticmethod
    def get_phone_number(obj):
        return parse_phone_number(obj.phone_number)

    class Meta:
        model = Student
        exclude = ['updated_at']
