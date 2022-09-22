from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from apps.donate.filters import AdminDonateFilter
from apps.donate.models import Donate
from apps.donate.serializers.admin import AdminDonateListSerializer


class AdminDonateListView(generics.ListAPIView):
    """Admin homiylar ro'xatini ko'rish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminDonateListSerializer
    queryset = Donate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdminDonateFilter
