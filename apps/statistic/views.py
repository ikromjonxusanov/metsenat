from django.db.models import Sum, Prefetch
from rest_framework import views, permissions
from rest_framework.response import Response

from apps.donate.models import DonatesForStudent
from apps.student.models import Student


class AdminMainStatisticsView(views.APIView):
    """Admin asosiy statistika qismi"""
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        payed_amount = Student.objects.prefetch_related(
            Prefetch('donater_for_student', queryset=DonatesForStudent.objects.only('amount'))
        ).aggregate(amount=Sum('donater_for_student__amount'))['amount']
        asked_amount = Student.objects.aggregate(amount=Sum('contract_amount'))['amount']
        needed_amount = asked_amount - payed_amount
        return Response({
            "payed_amount": payed_amount,
            "asked_amount": asked_amount,
            "needed_amount": needed_amount
        })
