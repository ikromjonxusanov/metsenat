from django.db.models import Sum, Prefetch
from django.db.models.functions import Coalesce

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter

from apps.donate.filters import AdminDonateFilter
from apps.donate.models import Donate, DonatesForStudent
from apps.donate.serializers.admin import AdminDonateListSerializer, AdminDonateRetrieveSerializer, \
    AdminDonateEditSerializer


class AdminDonateListView(generics.ListAPIView):
    """Admin homiylar ro'xatini ko'rish qismi"""
    # permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminDonateListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdminDonateFilter
    search_fields = ['fio']

    def get_queryset(self):
        return Donate.objects.annotate(
            spent_amount=Coalesce(Sum('donater__amount'), 0)
        ).prefetch_related(
            Prefetch("donater", queryset=DonatesForStudent.objects.only('amount'))
        )


class AdminDonateRetrieveView(generics.RetrieveAPIView):
    """Admin homiyni ko'rish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminDonateRetrieveSerializer
    queryset = Donate.objects.all()


class AdminDonateEditView(generics.UpdateAPIView):
    """Admin homiyni ma'lumotlarini o'zgartirish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminDonateEditSerializer
    queryset = Donate.objects.all()
