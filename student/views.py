import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, exceptions, serializers
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

from StudentManageSys import settings
from coupon.models import Coupon, StudentCoupon
from order.models import Order
from student.filters import StudentInfoFilterSet
from student.functions import change_student_status
from student.models import StudentInfo, StudentScoreDetail, StudentAgreement
from student.serializers import StudentInfoSerializer, StudentScoreDetailSerializer, StudentAgreementSerializer
from utils.weixin_functions import WxInterfaceUtil


class StudentInfoViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    filter_class = StudentInfoFilterSet

    @list_route()
    def send(request, self):
        msg = '<a href="哈哈哈" target="_blank">点击激活</a>'
        send_mail('标题', '内容', settings.EMAIL_FROM,
                  ['kimyeee@163.com'],
                  html_message=msg)
        return HttpResponse('ok')

    def get_queryset(self):
        if self.request.query_params.get('all_payment_student'):
            return self.queryset.filter(student_status__in=['PAYMENT_CONFIRMED', 'COMPLETE_FILE',
                                                            'UPLOAD_FILE', 'TO_CHOOSE_COURSE', 'UPLOAD_CONFIRM',
                                                            'CONFIRM_POSTIL', 'PICKUP_COURSE', 'IN_CLASS',
                                                            'AFTER_SCORE', 'POSTING', 'SWITCHED_COURSE'])
        return super().get_queryset()

    @list_route()
    def clear(self, request):
        student_id = request.query_params.get('id')
        StudentScoreDetail.objects.filter(user_id=student_id).delete()

        StudentInfo.objects.filter(id=student_id).delete()
        return HttpResponse('ok')

    @list_route(['GET'])
    def authorize(self, request):
        """客户端登录获取授权"""
        code = request.query_params.get('code')
        if not code:
            raise serializers.ValidationError('Param code is none')
        res = WxInterfaceUtil.code_authorize(code)
        user_id = res.get('user_id')
        student_status = StudentInfo.objects.filter(id=user_id).values('student_status').first().get('student_status')
        response = Response({'user_id': user_id, 'student_status': student_status})
        response.setdefault('token', res.get('token'))
        response['Access-Control-Expose-Headers'] = 'token'
        return response

    # @list_route(['GET'], serializer_class=GetUserInfoSerializer)
    # def take_user_info(self, request):
    #     serializer = self.serializer_class()
    #     serializer.get_user_info(request)
    #     return Response('补全用户信息成功 ')

    @list_route()
    def check_user_info(self, request):
        user = request.user
        user_info = StudentInfo.objects.filter(user=user).first()
        if not user_info:
            raise exceptions.ValidationError('不存在基础的用户信息')
        if all([user_info.name, user_info.email, user_info.wechat, user_info.wcampus]) is False:
            need_complete_stu_info = True
        else:
            need_complete_stu_info = False
        return Response({
            'need_complete_stu_info': need_complete_stu_info,
            'user_id': user.id,
            "valid_sales_man": True if user_info.valid_sales_man else False
        })

    @detail_route()
    def coupon_list(self, request, pk):
        """
        获取用户优惠券
        :param request:
        :return:
        """
        user = request.user
        current_time = datetime.datetime.now()
        res = Coupon.objects.filter(studentcoupon__user=user, status="TO_USE").exclude(
            end_time__lt=current_time).values()
        return Response(res)


class StudentScoreDetailViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    """成绩单寄送地址视图"""
    queryset = StudentScoreDetail.objects.all()
    serializer_class = StudentScoreDetailSerializer

    # pagination_class = None

    def get_queryset(self):
        user_id = self.request.query_params.get('user')
        if user_id:
            queryset = self.queryset.filter(user_id=user_id)
        else:
            queryset = self.queryset.filter(user=self.request.user)
        return queryset


class StudentAgreementView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = StudentAgreement.objects.all()
    serializer_class = StudentAgreementSerializer
