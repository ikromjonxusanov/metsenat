from rest_framework import serializers
from apps.donate.models import Donate


class AdminDonateListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Donate
        exclude = ['user_type', 'updated_at']
