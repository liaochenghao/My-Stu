import base64
import uuid

from django.db import transaction
from rest_framework import serializers, mixins, viewsets, exceptions
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from StudentManageSys import settings
from course.models import Course
from project.models import ProjectCourse, Project
from student.functions import change_student_status
from student.models import StudentInfo
from student_course.models import Review, ReviewCourse, ConfirmCourse, ChangeCourseRecord
from student_course.serializers import ReviewSerializer, ReviewCourseSerializer, ConfirmCourseSerializer, \
    ChangeCourseRecordSerializer
from user_info.models import UserInfo
from utils.common import append_url_with_domain


class ReviewView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                 mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def create(self, request, *args, **kwargs):
    #     super().create(request, *args, **kwargs)
    #     student_id = request.data['student']
    #     change_student_status(student_id=student_id, status='TO_CHOOSE_COURSE')
    #     return Response()

    @list_route()
    def get_review(self, request):
        """根据学生id获取审课方案"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            raise serializers.ValidationError('参数(student_id)不能为空')
        reviews = self.queryset.filter(student=student_id).values()
        return Response(reviews)


class ReviewCourseView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                       mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = ReviewCourse.objects.all()
    serializer_class = ReviewCourseSerializer

    # def create(self, request, *args, **kwargs):
    #     course_id = request.data['course']
    #     name = Course.objects.filter(id=course_id).values('name').first()
    #     request.data['real_name'] = name['name']
    #     return super().create(request, *args, **kwargs)

    @list_route(['POST'])
    @transaction.atomic()
    def add_review_course(self, request):
        """为学生创建审课方案"""
        course = request.data.get('course')
        if not course[0]['student_id']:
            raise serializers.ValidationError('参数student_id不能为空')
        student = StudentInfo.objects.filter(id=course[0]['student_id']).first()
        student_server = UserInfo.objects.first()
        # student_server = request.user
        review = Review.objects.create(student=student, student_server=student_server)
        change_student_status(student_id=course[0]['student_id'], status='TO_CHOOSE_COURSE')
        for cou in course:
            course = Course.objects.filter(id=cou['course_id']).first()
            real = Course.objects.filter(id=cou['course_id']).values('course_code', 'name').first()
            ReviewCourse.objects.create(course_name=cou['course_name'], course_code=real['course_code'], review=review,
                                        course=course, school=cou['school'], real_name=real['name'],
                                        student_id=cou['student_id'], status='WAIT_CERTIFICATE')
            ReviewCourse.objects.filter(student_id=cou['student_id'], course_code=real['course_code']).update(
                status='WAIT_CERTIFICATE')
        return Response('创建成功！')

    @list_route()
    def get_review_course(self, request):
        """根据学生id获取学生审课方案表"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            raise serializers.ValidationError('参数(student_id)不能为空')
        review_list = Review.objects.filter(student=student_id).values('id', 'create_time', 'modified_time')
        review_courses = self.queryset.filter(review__in=[data['id'] for data in review_list]).values('id', 'review',
                                                                                                      'school',
                                                                                                      'course_code',
                                                                                                      'course_name',
                                                                                                      'course__name',
                                                                                                      'status',
                                                                                                      'review_certificate',
                                                                                                      'real_name')
        result = list(review_list)
        for review in result:
            review['course_detail'] = []
            for course in review_courses:
                if course['review'] == review['id']:
                    review['course_detail'].append(course)
        return Response(result)

    @list_route()
    def confirm_review_course(self, request):
        """学服确认学生审课成功"""
        student_id = request.query_params.get('student_id')
        course_code = request.query_params.get('course_code')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(student_id, course_code)不能为空')
        self.queryset.filter(course_code=course_code, student_id=student_id).update(
            status='SUCCESS')
        result = self.queryset.filter(student_id=student_id, status__in=['WAIT', 'WAIT_CERTIFICATE']).exclude(
            status='FAIL')
        if not result:
            change_student_status(student_id=student_id, status='PICKUP_COURSE')
        return Response('操作成功!')

    @list_route()
    def deny_review_course(self, request):
        """学服确认学生审课失败"""
        course_code = request.query_params.get('course_code')
        student_id = request.query_params.get('student_id')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(student_id, course_code)不能为空')
        self.queryset.filter(course_code=course_code, student_id=student_id).update(
            status='FAIL')
        # TODO 判断学生状态是否回到沟通选课
        return Response('操作成功!')

    @list_route(['POST'])
    def upload_certificate(self, request):
        """用户上传审课凭据"""
        course_code = request.data.get('course_code')
        course_name = request.data.get('course_name')
        certificate = request.data.get('certificate')
        remark = request.data.get('remark')
        if not all([course_code, certificate, course_name]):
            raise serializers.ValidationError('参数(course_name, course_code, certificate)不能为空')
        review_course = ReviewCourse.objects.filter(course_code=course_code, course_name=course_name,
                                                    student_id=request.user.id)
        if not review_course:
            raise serializers.ValidationError('该课程不存在')
        if certificate:
            image_base64 = str(certificate)[str(certificate).find(',') + 1:]
            image_data = base64.b64decode(image_base64)
            file_name = str(uuid.uuid4()) + '.' + str(certificate)[
                                                  str(certificate).find('/') + 1:str(certificate).find(';')]
            abs_path = '%s/images/certificate/%s' % (settings.MEDIA_ROOT, file_name)
            with open(abs_path, 'wb') as pic:
                pic.write(image_data)
            review_course.update(status='WAIT', review_certificate='images/certificate/%s' % file_name,
                                 remark=remark)
            change_student_status(student_id=request.user.id, status='UPLOAD_CONFIRM')
            return Response('审课凭据上传成功！')
        return Response('certificate有误')

    @list_route()
    def get_certificate(self, request):
        """查看用户审课凭据"""
        course_code = request.query_params.get('course_code')
        student_id = request.query_params.get('student_id')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(student_id, course_code)不能为空')
        review_certificate = ReviewCourse.objects.filter(course_code=course_code, student_id=student_id).first()
        result = ReviewCourseSerializer(review_certificate).data
        return Response({'review_certificate': append_url_with_domain(result['review_certificate'])})


class ConfirmCourseView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                        mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = ConfirmCourse.objects.all()
    serializer_class = ConfirmCourseSerializer
    filter_fields = ('student_id',)

    @list_route()
    def review_project(self, request):
        """根据学生id获取审课-项目信息"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            raise serializers.ValidationError('参数student_id不能为空')
        reviewcourse = ReviewCourse.objects.filter(student_id=student_id, status='SUCCESS').values('course_name',
                                                                                                   'course_code',
                                                                                                   'school', 'course',
                                                                                                   'course__name')
        course_list = [data['course'] for data in reviewcourse]
        project = ProjectCourse.objects.filter(course__in=course_list).values('project', 'project__name', 'course',
                                                                              'project__course_num')
        for rev in reviewcourse:
            rev['project'] = []
            for pro in project:
                if rev['course'] == pro['course']:
                    rev['project'].append(pro)
        return Response(reviewcourse)


    @list_route(['POST'])
    @transaction.atomic()
    def add_course(self, request):
        """给学生添加课程"""
        student_id = request.data.get('student_id')
        course_name = request.data.get('course_name')
        school = request.data.get('school')
        course_id = request.data.get('course_id')
        project_id = request.data.get('project_id')
        course_code = request.data.get('course_code')
        change_type = request.data.get('change_type')
        extra = request.data.get('extra')
        if not student_id:
            raise serializers.ValidationError('参数student_id不能为空')
        student = StudentInfo.objects.filter(id=student_id).first()
        student_server = UserInfo.objects.first()
        # student_server = request.user
        change_type = change_type if change_type else '加课'
        project_course = ProjectCourse.objects.filter(project=project_id, course=course_id).first()
        course = Course.objects.filter(id=course_id).values('name').first()['name']
        project = Project.objects.filter(id=project_id).values('name').first()['name']
        confirm = ConfirmCourse.objects.create(student=student, project_course=project_course, course_name=course_name,
                                               school=school, course_code=course_code, status='NOTHING')
        change = ChangeCourseRecord.objects.create(student=student, course_name=course_name, course=course,
                                                   student_server=student_server, project=project, school=school,
                                                   course_code=course_code, change_type=change_type, extra=extra)
        return Response(ConfirmCourseSerializer(confirm).data)

    @list_route(['PATCH'])
    def score_recipient(self, request):
        """录入学生成绩等级或快递信息"""
        confirm_id = request.data.get('id')
        student_id = request.data.get('student_id')
        course_code = request.data.get('course_code')
        score = request.data.get('score')
        grade = request.data.get('grade')
        recipient_number = request.data.get('recipient_number')
        sending_date = request.data.get('sending_date')
        if not all([student_id, course_code]):
            raise serializers.ValidationError('参数(student_id, course_code)不能为空')
        if score and grade:
            status = 'SCORE_WAIT'
            self.queryset.filter(student=student_id, course_code=course_code).update(score=score, grade=grade,
                                                                                     status=status)
            result = self.queryset.filter(student_id=student_id, status='NOTHING')
            if not result:
                change_student_status(student_id=student_id, status='AFTER_SCORE')
        if recipient_number and sending_date:
            convert_status = 'SENT'
            self.queryset.filter(id=confirm_id).update(convert_status=convert_status, recipient_number=recipient_number,
                                                       sending_date=sending_date)
            result = self.queryset.filter(student_id=student_id, convert_status__in=['NO_SEND', 'RECEIVED'])
            if not result:
                change_student_status(student_id=student_id, status='POSTING')
        return Response('操作成功')

    @list_route()
    def get_server_time(self, request):
        """根据学生id获取学服老师及确认课程时间"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            raise serializers.ValidationError('参数(student_id)不能为空')
        result = self.queryset.filter(student=student_id).values('student__server', 'modified_time').first()
        return Response(result)

    # @list_route()
    # def get_confirm_course(self, request):
    #     """根据学生id获取确认课程"""
    #     student_id = request.query_params.get('student_id')
    #     if not student_id:
    #         raise serializers.ValidationError('参数(student_id)不能为空')
    #     data = self.queryset.filter(student=student_id).values('id', 'course_code', 'course_name', 'school',
    #                                                            'project_course__course__name',
    #                                                            'project_course__address', 'project_course__start_time',
    #                                                            'project_course__project__name')
    #     return Response(data)

    @list_route()
    def get_select_student(self, request):
        """获取开课列表选课学生名单"""
        project_course_id = request.query_params.get('project_course_id')
        page = int(request.query_params.get('page'))
        page_size = int(request.query_params.get('page_size'))
        if not all([project_course_id, page, page_size]):
            raise serializers.ValidationError('参数(project_course_id, page, page_size)不能为空')
        select_num = ConfirmCourse.objects.filter(project_course=project_course_id).count()
        result = ConfirmCourse.objects.filter(project_course=project_course_id).select_related('student').values(
            'student__id_number', 'student__name', 'student__cc', 'student__cschool', 'student__server')[
                 (page - 1) * page_size:page * page_size]
        data = {}
        data['select_num'] = select_num
        data['result'] = result
        return Response(data)

    # @list_route()
    # def query_performance(self, request):
    #     """根据学生id查询成绩"""
    #     student_id = request.query_params.get('student_id')
    #     if not student_id:
    #         raise serializers.ValidationError('参数(student_id)不能为空')
    #     data = self.queryset.filter(student=student_id).values('course_code', 'course_name', 'school', 'score', 'grade',
    #                                                            'score_enter_time', 'status', 'modified_time',
    #                                                            'project_course__course__name',
    #                                                            'project_course__project__name')
    #     return Response(data)

    @list_route()
    def confirm_performance(self, request):
        """学生确认成绩"""
        course_code = request.query_params.get('course_code')
        course_name = request.query_params.get('course_name')
        if not all([course_code, course_name]):
            raise serializers.ValidationError('参数(course_name, course_code)不能为空')
        self.queryset.filter(course_code=course_code, course_name=course_name, student_id=request.user.id).update(
            status='CONFIRMED', convert_status='NO_SEND')
        data = self.queryset.filter(course_code=course_code, course_name=course_name,
                                    student_id=request.user.id).values('status', 'modified_time').first()
        return Response(data)

    # @list_route()
    # def get_recipient(self, request):
    #     """根据学生id查询快递"""
    #     student_id = request.query_params.get('student_id')
    #     if not student_id:
    #         raise serializers.ValidationError('参数(student_id)不能为空')
    #     data = self.queryset.filter(student=student_id).values('id', 'course_code', 'course_name', 'image',
    #                                                            'convert_status', 'project_course__course_name',
    #                                                            'school', 'project_course__project__name', 'score',
    #                                                            'grade', 'recipient_number', 'sending_date')
    #     return Response(data)

    # @list_route()
    # def get_student_convert(self, request):
    #     """根据学生id获取学分转换信息"""
    #     student_id = request.query_params.get('student_id')
    #     if not student_id:
    #         raise serializers.ValidationError('参数(student_id)不能为空')
    #     data = self.queryset.filter(student=student_id).values('course_code', 'convert_status', 'course_name', 'school',
    #                                                            'image', 'recipient_number', 'sending_date',
    #                                                            'project_course__project__name')
    #     return Response(data)

    @list_route(['POST'])
    def upload_convert(self, request):
        """学生上传转学分图片"""
        course_code = request.data.get('course_code')
        course_name = request.data.get('course_name')
        image = request.data.get('image')
        remark = request.data.get('remark')
        if not all([course_code, course_name, image]):
            raise serializers.ValidationError('参数(course_code, course_name, image)不能为空')
        confirm_course = ConfirmCourse.objects.filter(course_code=course_code, course_name=course_name,
                                                      student_id=request.user.id)
        if not confirm_course:
            raise serializers.ValidationError('该课程不存在')
        if image:
            image_base64 = str(image)[str(image).find(',') + 1:]
            image_data = base64.b64decode(image_base64)
            file_name = str(uuid.uuid4()) + '.' + str(image)[str(image).find('/') + 1:str(image).find(';')]
            abs_path = '%s/images/convert/%s' % (settings.MEDIA_ROOT, file_name)
            with open(abs_path, 'wb') as pic:
                pic.write(image_data)
            confirm_course.update(convert_status='CONVERT_WAIT', image='images/convert/%s' % file_name, remark=remark)
            return Response('转学分图片上传成功！')
        return Response('image有误')

    @list_route()
    def get_convert(self, request):
        """查看用户转学分图片"""
        student_id = request.query_params.get('student_id')
        course_code = request.query_params.get('course_code')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(course_code, student_id)不能为空')
        confirm_course = ConfirmCourse.objects.filter(course_code=course_code, student=student_id).first()
        result = ConfirmCourseSerializer(confirm_course).data
        return Response({'image': append_url_with_domain(result['image'])})

    @list_route()
    def confirm_convert(self, request):
        """学服确认学生转学分成功"""
        student_id = request.query_params.get('student_id')
        course_code = request.query_params.get('course_code')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(course_code, student_id)不能为空')
        self.queryset.filter(course_code=course_code, student_id=student_id).update(status='SUCCESS')
        result = self.queryset.filter(student_id=student_id, convert_status__in=['CONVERT_WAIT', 'WAIT_IMAGE']).exclude(
            convert_status='FAIL')
        if not result:
            change_student_status(student_id=student_id, status='SWITCHED_COURSE')
        return Response('操作成功!')

    @list_route()
    def deny_convert(self, request):
        """学服确认学生转学分失败"""
        student_id = request.query_params.get('student_id')
        course_code = request.query_params.get('course_code')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(course_code, student_id)不能为空')
        self.queryset.filter(course_code=course_code, student_id=student_id).update(convert_status='FAIL')
        return Response('操作成功!')


class ChangeCourseRecordView(mixins.CreateModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                             mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = ChangeCourseRecord.objects.all()
    serializer_class = ChangeCourseRecordSerializer

    # @list_route(['POST'])
    # @transaction.atomic()
    # def add_change(self, request):
    #     """给学生添加调课记录"""
    #     student_id = request.data.get('student_id')
    #     course_name = request.data.get('course_name')
    #     school = request.data.get('school')
    #     course = request.data.get('course')
    #     project = request.data.get('project')
    #     course_code = request.data.get('course_code')
    #     change_type = request.data.get('change_type')
    #     extra = request.data.get('extra')
    #     if not student_id:
    #         raise serializers.ValidationError('参数student_id不能为空')
    #     student = StudentInfo.objects.filter(id=student_id).first()
    #     student_server = UserInfo.objects.first()
    #     # student_server = request.user
    #     data = ChangeCourseRecord.objects.create(student=student, course_name=course_name, course=course,
    #                                              student_server=student_server, project=project, school=school,
    #                                              course_code=course_code, change_type=change_type, extra=extra)
    #     return Response(ChangeCourseRecordSerializer(data).data)

    @transaction.atomic()
    @list_route(['POST'])
    def del_course(self, request):
        """删除学生课程"""
        student_id = request.data.get('student_id')
        course_code = request.data.get('course_code')
        extra = request.data.get('extra')
        if not all([course_code, student_id]):
            raise serializers.ValidationError('参数(course_code, student_id)不能为空')
        confirm = ConfirmCourse.objects.filter(student=student_id, course_code=course_code)
        datas = confirm.values('course_name', 'project_course', 'school').first()
        names = ProjectCourse.objects.filter(id=datas['project_course']).values('course__name', 'project__name').first()
        student = StudentInfo.objects.filter(id=student_id).first()
        student_server = UserInfo.objects.first()
        # student_server = request.user
        ChangeCourseRecord.objects.create(student_server=student_server, student=student,
                                          course_name=datas['course_name'], course_code=course_code, change_type='删课',
                                          extra=extra, course=names['course__name'], project=names['project__name'],
                                          school=datas['school'])
        confirm.delete()
        return Response("操作成功!")

    @list_route()
    def get_change_record(self, request):
        """根据学生id获取课程调整记录"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            raise serializers.ValidationError('参数(student_id)不能为空')
        change_record = self.queryset.filter(student=student_id).values('student_server', 'course_code', 'course_name',
                                                                        'project', 'course', 'school', 'modified_time',
                                                                        'change_type', 'extra')
        return Response(change_record)
