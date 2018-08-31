from rest_framework import serializers

from course.models import Course


class OperationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'operator', 'operation', 'target', 'ip_address', 'description', 'create_time', 'operator_type']
