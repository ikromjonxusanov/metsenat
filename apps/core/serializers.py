from rest_framework import serializers

from apps.core.models import OTM


class OTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTM
        fields = "__all__"
