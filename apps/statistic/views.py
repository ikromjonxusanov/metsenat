from django.db.models import Sum, Prefetch, Count
from django.db.models.functions import TruncMonth, TruncDay
from rest_framework import views, permissions
from rest_framework.response import Response

from apps.donate.models import DonatesForStudent, Donate
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


class AdminDateStatistics(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        students_months = Student.objects.annotate(month=TruncMonth('created_at')) \
            .values('month') \
            .annotate(count=Count('id')) \
            .values('month', 'count')
        donates_months = Donate.objects.annotate(month=TruncMonth('created_at')) \
            .values('month') \
            .annotate(count=Count('id')) \
            .values('month', 'count')
        students_days = Student.objects.annotate(day=TruncDay('created_at')) \
            .values('day') \
            .annotate(count=Count('id')) \
            .values('day', 'count')
        donates_days = Donate.objects.annotate(day=TruncDay('created_at')) \
            .values('day') \
            .annotate(count=Count('id')) \
            .values('day', 'count')

        return Response({
            "students_months": students_months,
            "donates_months": donates_months,
            "students_days": students_days,
            "donates_days": donates_days,
        })
