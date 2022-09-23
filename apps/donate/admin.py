from django.contrib import admin

from apps.donate.models import Donate, DonatesForStudent
from apps.student.models import Student


@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number']


@admin.register(DonatesForStudent)
class DonatesForStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'donater', 'student', 'amount']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number', 'contract_amount']
