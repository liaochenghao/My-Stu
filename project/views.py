# Create your views here.
from rest_framework import mixins, viewsets, serializers
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from campus.models import Campus
from course.models import Course
from project.models import Project, ProjectCourse
from project.serializers import ProjectSerializer, ProjectCourseSerializer
from student_course.models import ConfirmCourse, ReviewCourse


class ProjectView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                  mixins.ListModelMixin, mixins.UpdateModelMixin):
    """项目视图"""
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    filter_fields = ['campus']

    def create(self, request, *args, **kwargs):
        campus_id = request.data.get('campus')
        request.data['campus_name'] = Campus.objects.filter(id=campus_id).first().name
        return super().create(request, *args, **kwargs)

    @list_route()
    def get_project_by_campus(self, request):
        """根据校区id搜索项目"""
        campus_id = request.query_params.get('campus_id')
        if not campus_id:
            raise serializers.ValidationError('参数(campus_id)不能为空')
        project = Project.objects.filter(campus_id=campus_id).values()
        return Response(project)

    @list_route(['GET'])
    def all(self, request):
        return Response(Project.objects.all().values('id', 'name'))


class ProjectCourseView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """项目课程关联视图"""
    queryset = ProjectCourse.objects.filter(status=True).all()
    serializer_class = ProjectCourseSerializer
    filter_fields = ['project', 'course', 'campus_id']

    def create(self, request, *args, **kwargs):
        project_id = request.data.get('project')
        datas = Project.objects.filter(id=project_id).values('campus', 'campus_name').first()
        if datas:
            request.data['campus_id'] = datas['campus']
        return super().create(request, *args, **kwargs)

    @list_route()
    def get_course(self, request):
        """课程管理模块根据项目id搜索课程"""
        project_id = request.query_params.get('project_id')
        if not project_id:
            raise serializers.ValidationError('参数(project_id)不能为空')
        data = self.queryset.filter(project=project_id).values('course', 'course_name', 'create_time',
                                                               'modified_time')
        return Response(data)

    @list_route()
    def get_project(self, request):
        """根据课程id搜索项目"""
        course_id = request.query_params.get('course_id')
        if not course_id:
            raise serializers.ValidationError('参数(course_id)不能为空')
        data = self.queryset.filter(course=course_id).values('project', 'project__name')
        return Response(data)

    @list_route()
    def relate_review_course(self, request):
        """查看关联审课课程"""
        course_id = request.query_params.get('course_id')
        if not course_id:
            raise serializers.ValidationError('参数(course_id)不能为空')
        course_code = Course.objects.filter(id=course_id).values('course_code').first()['course_code']
        datas = ReviewCourse.objects.filter(course_code=course_code).values('school', 'course_code', 'course_name',
                                                                            'real_name')

        # project_course_id = [data['id'] for data in datas]
        # confirm_course = ConfirmCourse.objects.filter(project_course__in=project_course_id, status=True).values_list(
        #     'project_course', flat=True)
        # for res in datas:
        #     for con in list(confirm_course):
        #         if res['id'] == con:
        #             res['select_course_num'] = list(confirm_course).count(con)
        return Response(datas)
