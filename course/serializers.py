from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'course_code', 'name', 'extra', 'credit', 'create_time', 'modified_time']


