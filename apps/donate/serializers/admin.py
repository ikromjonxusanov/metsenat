from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import serializers

from apps.core.helpers import parse_phone_number
from apps.core.validators import PhoneValidator
from apps.donate.models import Donate, DonatesForStudent


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


class StudentDonaterListSerializer(serializers.ModelSerializer):
    donater = serializers.CharField(source='donater.fio', read_only=True)

    class Meta:
        model = DonatesForStudent
        fields = ['id', 'donater', 'amount']


class AdminDonateForStudentAddSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField(min_value=0, max_value=9223372036854775807)

    class Meta:
        model = DonatesForStudent
        fields = ['donater', 'student', 'amount']

    def validate(self, attrs):
        student = attrs.get('student')
        donater = attrs.get('donater')

        allocated_amount = student.donater_for_student.aggregate(
            amount=Coalesce(Sum('amount'), 0),
        )['amount']

        amount = student.contract_amount - allocated_amount

        donate_amount = donater.donater.aggregate(
            amount=Coalesce(Sum('amount'), 0),
        )['amount']

        donater_amount = donater.donate_amount - donate_amount
        if donater_amount == 0:
            raise serializers.ValidationError({"amount": "Homiyni mablag'i ishlatilgan"})
        elif attrs.get('amount') > donater_amount:
            raise serializers.ValidationError({"amount": "Homiyni mablag'i yetarli emas"})
        elif amount == 0:
            raise serializers.ValidationError({"amount": "Talabani kantrakiga yetarli pul yig'ilgan"})
        elif attrs.get('amount') <= amount:
            return attrs
        raise serializers.ValidationError({'amount': f"Eng ko'pida {amount} so'm miqdorda homiylik qilish mumkin"})


class AdminDonateForStudentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatesForStudent
        fields = ['donater', 'amount']

    def update(self, instance, validated_data):
        donater = validated_data.get('donater', instance.donater)
        student = instance.student
        amount = validated_data.get('amount', instance.amount)

        allocated_amount = student.donater_for_student.aggregate(
            amount=Coalesce(Sum('amount'), 0),
        )['amount']

        donate_amount = donater.donater.aggregate(
            amount=Coalesce(Sum('amount'), 0),
        )['amount']

        donater_amount = donater.donate_amount - donate_amount

        if instance.amount != amount:
            donater_amount += instance.amount - amount
            allocated_amount -= instance.amount

        need_amount = student.contract_amount - allocated_amount

        if amount > donater_amount:
            raise serializers.ValidationError({"amount": "Homiyni mablag'i yetarli emas"})
        elif need_amount == 0:
            raise serializers.ValidationError({"amount": "Talabani kantrakiga yetarli pul yig'ilgan"})
        elif amount <= need_amount:
            return super().update(instance, validated_data)
        raise serializers.ValidationError({'amount': f"Eng ko'pida {need_amount} so'm miqdorda homiylik qilish mumkin"})
