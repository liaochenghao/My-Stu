# Create your views here.
from rest_framework import exceptions, mixins, viewsets, serializers
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from course.models import Course
from course.serializers import CourseSerializer
from project.models import ProjectCourse


class CourseView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                 mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Course.objects.all().filter(is_active=True).prefetch_related('projectcourse_set',
                                                                            'projectcourse_set__project')
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project = self.request.query_params.get('project')
        if not project:
            return queryset
        if not str(project).isdigit():
            raise serializers.ValidationError('参数有误')
        course_ids = ProjectCourse.objects.filter(project_id=project).values_list('course_id', flat=True)
        queryset = queryset.filter(id__in=course_ids)
        return queryset

    @list_route(['GET'])
    def all(self, request):
        return Response(Course.objects.all().values('id', 'course_code', 'name'))
