from rest_framework import serializers

from apps.core.validators import PhoneValidator
from apps.donate.helpers import parse_phone_number
from apps.donate.models import Donate


class AdminDonateListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    phone_number = serializers.SerializerMethodField()
    spent_amount = serializers.IntegerField(read_only=True)

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


class AdminDonateEditSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(min_length=9, max_length=9, validators=[PhoneValidator()])
    donate_amount = serializers.IntegerField(min_value=0, max_value=9223372036854775807)

    class Meta:
        model = Donate
        fields = [
            'fio', 'phone_number', 'user_type', 'status', 'donate_amount', 'organization',
        ]

    def validate(self, attrs):
        if attrs.get('user_type') == Donate.UserType.Y and attrs.get('organization') is None:
            raise serializers.ValidationError({
                'organization': "Siz Yuridik shaxs tomonidan murojaat "
                                "qilyapsiz iltimos Tashkilot nomini kiriting"
            })
        return attrs
