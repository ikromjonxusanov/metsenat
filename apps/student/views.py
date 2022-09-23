from django.db.models import Prefetch, Sum
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from apps.core.models import OTM
from apps.donate.models import DonatesForStudent, Donate
from apps.student.filters import AdminStudentFilter
from apps.student.models import Student
from apps.student.serializers import AdminStudentAddSerializer, AdminStudentListSerializer, \
    AdminStudentRetrieveSerializer


class AdminStudentAddView(generics.CreateAPIView):
    """Admin talabani qo'shish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminStudentAddSerializer


class AdminStudentListView(generics.ListAPIView):
    """Admin talabalar ro'yxatini ko'rish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminStudentListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdminStudentFilter

    def get_queryset(self):
        return Student.objects.annotate(
            allocated_amount=Coalesce(Sum('donater_for_student__amount'), 0)
        ).prefetch_related(
            Prefetch('otm', queryset=OTM.objects.only('name')),
            Prefetch('donater_for_student', queryset=DonatesForStudent.objects.only('amount'))
        )


class AdminStudentRetrieveView(generics.RetrieveAPIView):
    """Admin talaba haqida to'liq ma'lumot olish qismi"""
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminStudentRetrieveSerializer

    def get_queryset(self):
        return Student.objects.annotate(
            allocated_amount=Coalesce(Sum('donater_for_student__amount'), 0)
        ).prefetch_related(
            Prefetch('otm', queryset=OTM.objects.only('name')),
            Prefetch('donater_for_student', queryset=DonatesForStudent.objects.only(
                'id', 'donater', 'amount'
            ).prefetch_related(Prefetch('donater', queryset=Donate.objects.only('fio'))))
        )
