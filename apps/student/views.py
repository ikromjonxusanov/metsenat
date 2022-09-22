from rest_framework import generics, permissions

from apps.student.serializers import AdminStudentAddSerializer


class AdminStudentAddView(generics.CreateAPIView):
    """Admin talabani qo'shish qismi"""
    permission_classes = [permissions.IsAdminUser]
    serializer_class = AdminStudentAddSerializer


