from rest_framework import generics, permissions
from apps.core.serializers import OTMSerializer
from apps.core.models import OTM


class AdminOTMListAndCreateView(generics.ListCreateAPIView):
    """Admin OTM lar ro'yxatini ko'rish va yaratish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = OTMSerializer
    queryset = OTM.objects.all()


class AdminOTMRetrieveEditAndDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Admin OTM ni ko'rish, o'zgartirish va o'chirish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = OTMSerializer
    queryset = OTM.objects.all()
