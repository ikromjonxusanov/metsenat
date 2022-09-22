from django.contrib import admin

from apps.donate.models import Donate


@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'phone_number']
