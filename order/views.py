from django.shortcuts import render

# coding: utf-8
import json

import datetime
from rest_framework import mixins, viewsets, exceptions
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from StudentManageSys.settings import DOMAIN, MEDIA_URL
from student.models import StudentInfo
from coupon.models import StudentCoupon, Coupon
from log_info.models import OperationLog
# from course.models import
from order.models import Order, OrderPayment, ShoppingChart, OrderCouponRelation, OrderAdditionalPayment, OrderRecord
from order.serializers import OrderSerializer, OrderPaymentSerializer, UserOrderCourseSerializer, \
    ShoppingChartSerializer, SimpleUserOrderSerializer, OrderAdditionalPaymentSerializer, OrderRecordSerializer

import logging

from utils.common import get_ip_address

logging = logging.getLogger("django")


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ['currency', 'payment', 'status', 'user']

    def get_serializer(self, *args, **kwargs):
        try:
            user = StudentInfo.objects.get(id=int(self.request.query_params.get('user')))  # 如果管理后台传入了user，则获取该user
        except Exception as e:
            user = self.request.user
        self.request.user = user
        return super().get_serializer(*args, **kwargs)

    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.query_params.get('none_canceled_order'):
    #         queryset = queryset.exclude(status='CANCELED')
    #     return queryset

    @list_route()
    def last_order(self, request):
        instance = self.queryset.filter(user=request.user).exclude(status='CANCELED').first()
        if instance:
            data = self.serializer_class(instance).data
            # order_chart_relations = instance.orderchartrelation_set.all()
            # courses_to_select_count = sum([order_chart.chart.course_num for order_chart in order_chart_relations])
            # course_current_selected_count = instance.usercourse_set.all().count()
            # data['course_to_select'] = True if instance.status == 'CONFIRMED' \
            #                                    and courses_to_select_count != course_current_selected_count else False
            if instance.create_time.replace(tzinfo=None) + datetime.timedelta(7) < datetime.datetime.now():
                data = {
                    "course_to_select": False
                }
                instance.status = 'CANCELED'
                instance.save()
        else:
            data = {
                "course_to_select": False
            }
        discount_amount = 0
        # if instance.coupon_list:
        #     coupons_amount = Coupon.objects.filter(id__in=json.loads(instance.coupon_list)).values_list(
        #         'amount')
        #     for coupon in coupons_amount:
        #         discount_amount += int(coupon[0])
        # data['coupon'] = discount_amount
        return Response(data)

    @list_route()
    def check_order(self, request):
        if self.queryset.filter(user=self.request.user, status__in=['TO_PAY', 'TO_CONFIRM']).exists():
            order_to = self.get_queryset().filter(user=self.request.user, status__in=['TO_PAY', 'TO_CONFIRM']).first()
            return Response(self.serializer_class(order_to).data)
        return Response({'code': 100, 'msg': '没有未完成的订单，可以创建'})

    @list_route()
    def order_currency_payment(self, request):
        """订单币种及支付方式"""
        data = [
            {
                'key': 'FOREIGN_CURRENCY',
                'verbose': dict(Order.CURRENCY).get('FOREIGN_CURRENCY'),
                'payment': [
                    {
                        'key': 'BANK',
                        'verbose': dict(Order.PAYMENT).get('BANK')
                    },
                    {
                        'key': 'PAY_PAL',
                        'verbose': dict(Order.PAYMENT).get('PAY_PAL')
                    }
                ]
            },
            {
                'key': 'RMB',
                'verbose': dict(Order.CURRENCY).get('RMB'),
                'payment': [
                    {
                        'key': 'BANK',
                        'verbose': dict(Order.PAYMENT).get('BANK')
                    },
                    {
                        'key': 'ALI_PAY',
                        'verbose': dict(Order.PAYMENT).get('ALI_PAY')
                    },
                    {
                        'key': 'OFF_LINE',
                        'verbose': dict(Order.PAYMENT).get('OFF_LINE')
                    }
                ]
            }
        ]
        return Response(data)

    @detail_route(['PUT'])
    def cancel(self, request, pk):
        """取消订单"""
        instance = self.get_object()
        if instance.status == 'CANCELED':
            raise exceptions.ValidationError('订单已被取消')
        elif instance.status != 'TO_PAY':
            raise exceptions.ValidationError('无法取消该订单')
        instance.status = 'CANCELED'
        instance.save()
        order_coupons = OrderCouponRelation.objects.filter(order=instance).values_list('coupon__coupon', flat=True)

        if order_coupons:
            # 如果使用了优惠券，将优惠券置为可用状态
            StudentCoupon.objects.filter(coupon_id__in=list(order_coupons)).update(status='TO_USE')
        OperationLog.objects.create(operator=request.user, operation=2, target=request.user.id,
                                    ip_address=get_ip_address(request), description='取消了订单')
        if request.user.student_status == 'SUPPLY_ORDER':
            request.user.student_status = 'PERSONAL_FILE'
            request.user.save()
        return Response(self.serializer_class(instance).data)

    @list_route()
    def user_order_list(self, request):
        """用户订单列表"""
        user = request.user
        status = self.request.query_params.get('status')
        none_canceled_order = self.request.query_params.get('none_canceled_order', True)
        user_orders = self.queryset.filter(user=user)
        if status:
            user_orders = user_orders.filter(status=status)
        if none_canceled_order:
            user_orders = user_orders.exclude(status='CANCELED')
        return Response(SimpleUserOrderSerializer(user_orders, many=True, context={'request': request}).data)

    @list_route()
    def user_order_course(self, request):
        self.serializer_class = UserOrderCourseSerializer
        user = request.user
        user_orders = self.queryset.filter(user=user)
        return Response(self.serializer_class(user_orders, many=True, context={'request': request}).data)


class OrderPaymentViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

    @list_route()
    def get_info(self, request):
        order_id = self.request.query_params.get('order_id')
        payment_info = self.queryset.filter(order_id=order_id).values().first()
        payment_info['img'] = DOMAIN + MEDIA_URL + payment_info.get('img')
        return Response(payment_info)


class OrderRecordViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    queryset = OrderRecord.objects.all()
    serializer_class = OrderRecordSerializer

    def get_queryset(self):
        student_id = self.request.query_params.get('student_id')
        queryset = self.queryset.filter(order__user_id=student_id)
        return queryset

    @list_route()
    def get_final_order(self, request):
        student_id = self.request.query_params.get('student_id')
        final_order = OrderRecord.objects.filter(order__user_id=student_id).order_by('-create_time').first()
        return Response(OrderRecordSerializer(final_order).data)


class OrderAdditionalPaymentViewSet(mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    viewsets.GenericViewSet):
    queryset = OrderAdditionalPayment.objects.all()
    serializer_class = OrderAdditionalPaymentSerializer
    filter_fields = ['type', 'refunded_type', 'replenish_type', 'status', 'currency']

    def create(self, request, *args, **kwargs):
        logging.info(request.data)
        logging.info('*' * 66)
        return super().create(request, *args, **kwargs)

    @list_route()
    def get_info(self, request):
        order_id = self.request.query_params.get('order_id')
        filter_type = self.request.query_params.get('type')
        payment_info_list = self.queryset.filter(order_id=order_id)
        if filter_type:
            payment_info_list = payment_info_list.filter(type=filter_type)
        return Response(OrderAdditionalPaymentSerializer(payment_info_list, many=True).data)


class ShoppingChartViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = ShoppingChart.objects.filter(status='NEW')
    serializer_class = ShoppingChartSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    @list_route(['PUT'])
    def update_charts(self, request):
        change_list = request.data
        for chart in change_list:
            ShoppingChart.objects.filter(id=chart.get('chart_id')).update(course_num=chart.get('course_num'))
        return Response('ok')

    @list_route()
    def get_user_project(self, request):
        student_id = self.request.query_params.get('student_id')
        # project_list = ShoppingChart.objects.filter(user_id=student_id, status='PAYED')
        project_list = OrderRecord.objects.filter(order__user_id=student_id).first()

        return Response(OrderRecordSerializer(project_list).data)

    @list_route(['DELETE'])
    def delete_charts(self, request):
        chart_ids = request.data.get('chart_ids')
        if not chart_ids:
            raise exceptions.ValidationError('缺少chart_ids参数')
        ShoppingChart.objects.filter(id__in=chart_ids).update(status='DELETED')
        return Response('ok')

    def perform_destroy(self, instance):
        instance.status = 'DELETED'
        instance.save()

    @list_route(['DELETE'])
    def shopping_chart_clear(self, request):
        self.get_queryset().update(status='DELETED')
        return Response({'msg': '请求成功'})
