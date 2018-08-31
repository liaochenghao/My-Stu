from rest_framework import serializers

from complain.models import Complain
from course.models import Course


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ['id', 'title', 'context', 'create_time']
