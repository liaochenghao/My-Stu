from rest_framework import serializers
from record.models import ChannelRecord, RecommendRecord


class ChannelRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelRecord
        fields = ['id', 'student_id', 'channel_id', 'create_time', 'status']


class RecommendRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendRecord
        fields = ['id', 'inviter', 'invitee', 'create_time', 'extra', 'status']
