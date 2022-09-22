from django_filters.rest_framework import FilterSet, filters
from apps.donate.models import Donate


class AdminDonateFilter(FilterSet):
    created_at_gt = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_lt = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    donate_amount = filters.ChoiceFilter(field_name='donate_amount', choices=(
        (1_000_000, "1 000 000"),
        (5_000_000, "5 000 000"),
        (7_000_000, "7 000 000"),
        (10_000_000, "10 000 000"),
        (30_000_000, "30 000 000"),
        (50_000_000, "50 000 000"),
    ))

    class Meta:
        model = Donate
        fields = ['status']
