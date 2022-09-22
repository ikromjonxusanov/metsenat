from rest_framework import generics, permissions
from django.db.models import Prefetch

from apps.core.models import OTM
from apps.student.models import Student
from apps.student.serializers import AdminStudentAddSerializer, AdminStudentListSerializer


class AdminStudentAddView(generics.CreateAPIView):
    """Admin talabani qo'shish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminStudentAddSerializer


class AdminStudentListView(generics.ListAPIView):
    """Admin talabalar ro'yxatini ko'rish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminStudentListSerializer

    def get_queryset(self):
        return Student.objects.prefetch_related(
            Prefetch('otm', queryset=OTM.objects.only('name'))
        )
