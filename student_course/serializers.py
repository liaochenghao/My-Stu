# coding: utf-8
from rest_framework import serializers

from student_course.models import Review, ReviewCourse, ConfirmCourse, ChangeCourseRecord


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'student', 'student_server', 'remark', 'create_time', 'modified_time']


class ReviewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewCourse
        fields = ['id', 'course_code', 'student_id', 'course_name', 'school', 'remark', 'review', 'status',
                  'course', 'review_certificate', 'real_name', 'create_time', 'modified_time']

    def create(self, validated_data):
        pass


class ConfirmCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmCourse
        fields = ['id', 'course_code', 'course_name', 'school', 'remark', 'student', 'create_time', 'project_course',
                  'score', 'modified_time', 'status', 'convert_status', 'score_enter_time', 'grade', 'image',
                  'recipient_number', 'sending_date']


class ChangeCourseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeCourseRecord
        fields = ['id', 'student', 'student_server', 'course_code', 'course_name', 'create_time', 'project', 'school',
                  'course', 'modified_time', 'change_type', 'extra']
