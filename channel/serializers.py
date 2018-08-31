from rest_framework import serializers

from channel.function import make_qrcode
from channel.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'sales_man', 'plan_date', 'plan_student_number', 'plan_file_student_number',
                  'plan_payed_student_number', 'phase_discount', 'channel_url', 'qr_code', 'create_time', 'update_time']

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.qr_code, instance.channel_url = make_qrcode(instance.id)
        instance.save()
        return instance
