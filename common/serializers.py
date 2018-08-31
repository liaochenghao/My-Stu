from rest_framework import serializers

from common.models import Common


class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = ['context', 'create_time']
