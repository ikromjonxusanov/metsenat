from rest_framework import serializers

from apps.donate.models import Donate


class DonateCreateSerializer(serializers.ModelSerializer):
    donate_amount = serializers.IntegerField(min_value=0, max_value=9223372036854775807)

    class Meta:
        model = Donate
        fields = [
            'fio', 'phone_number', 'organization', 'user_type', 'donate_amount',
        ]

    def validate(self, attrs):
        if attrs.get('user_type') == Donate.UserType.Y and attrs.get('organization') is None:
            raise serializers.ValidationError({
                'organization': "Siz Yuridik shaxs tomonidan murojaat "
                                "qilyapsiz iltimos Tashkilot nomini kiriting"
            })
        return attrs
