from rest_framework import serializers

from campus.models import Campus
from project.models import Project, ProjectCourse
from student_course.models import ConfirmCourse


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'campus', 'name', 'start_date', 'end_date', 'address', 'info', 'create_time',
                  'apply_fee', 'course_num', 'is_active', 'campus_name']


class ProjectCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCourse
        fields = ['id', 'modified_time', 'create_time', 'status', 'professor', 'start_time', 'end_time', 'address',
                  'course', 'project', 'course_name', 'course_code', 'max_select_num', 'campus_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        select_course_num = ConfirmCourse.objects.filter(project_course=data['id']).count()
        names = ProjectCourse.objects.filter(campus_id=data['campus_id'], project=data['project'], status=True).values(
            'project__name', 'project__campus__name', 'course__name').first()
        data['select_course_num'] = select_course_num
        data['real_name'] = names['course__name']
        data['campus_name'] = names['project__campus__name']
        data['project_name'] = names['project__name']
        data['select_course_num/max_select_num'] = str(select_course_num) + '/' + str(data['max_select_num'])
        return data
