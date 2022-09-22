from rest_framework import serializers

from apps.donate.helpers import parse_phone_number
from apps.donate.models import Donate


class AdminDonateListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    phone_number = serializers.SerializerMethodField()

    @staticmethod
    def get_phone_number(obj):
        return parse_phone_number(obj.phone_number)

    class Meta:
        model = Donate
        exclude = ['user_type', 'organization', 'updated_at']


class AdminDonateRetrieveSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    phone_number = serializers.SerializerMethodField()

    @staticmethod
    def get_phone_number(obj):
        return parse_phone_number(obj.phone_number)

    class Meta:
        model = Donate
        exclude = ['updated_at']
