from rest_framework import generics, permissions

from apps.donate.serializers.donater import DonateCreateSerializer


class DonateCreateView(generics.CreateAPIView):
    """Homiy bo'lish uchun zayafka qildirish"""
    permission_classes = [~permissions.IsAuthenticated]
    serializer_class = DonateCreateSerializer

