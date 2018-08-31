from rest_framework import serializers

from message.models import StudentMessage


class StudentMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMessage
        fields = ['id', 'student', 'message', 'create_time', 'status', 'update_time', 'type']
