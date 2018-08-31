# coding: utf-8
import datetime
import json

from django.db.models import Max

from StudentManageSys.settings import DOMAIN, MEDIA_URL
# from admin.functions import change_student_status
# from user_info.models import PaymentAccountInfo
from log_info.models import OperationLog
from payment.models import PaymentAccountInfo
from payment.serializers import PaymentAccountInfoSerializer
from student.functions import change_student_status
from student.models import StudentInfo, StudentScoreDetail
# from common.models import SalesMan
from coupon.models import StudentCoupon, Coupon
# from operate_history.functions import HistoryFactory
# from order.functions import order_auto_notice_message
from course.models import Course  # ,ProjectCourseFee
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from project.serializers import ProjectSerializer
from order.models import Order, OrderPayment, ShoppingChart, OrderChartRelation, OrderCouponRelation, \
    OrderAdditionalPayment, OrderRecord
from student_course.models import ConfirmCourse
from utils.common import get_ip_address
from utils.serializer_fields import VerboseChoiceField
import logging

logger = logging.getLogger('django')


# class PaymentAccountInfoSerializer(serializers.ModelSerializer):
#     """支付账号serializer"""
#     payment = VerboseChoiceField(PaymentAccountInfo.PAYMENT)
#     currency = VerboseChoiceField(PaymentAccountInfo.CURRENCY)
#
#     class Meta:
#         model = PaymentAccountInfo
#         fields = ['id', 'account_number', 'account_name', 'opening_bank', 'payment', 'currency', 'swift_code']


class OrderSerializer(serializers.ModelSerializer):
    """订单的serializer"""
    currency = VerboseChoiceField(choices=Order.CURRENCY, required=False)
    status = VerboseChoiceField(choices=Order.STATUS, required=False)
    payment = VerboseChoiceField(choices=Order.PAYMENT, required=False)
    chart_ids = serializers.ListField(write_only=True, child=serializers.IntegerField())

    class Meta:
        model = Order
        fields = ['id', 'currency', 'payment', 'status', 'remark', 'chart_ids', 'user', 'standard_fee', 'create_time',
                  'modified_time', 'order_number', 'pay_fee']
        read_only_fields = ['user', 'standard_fee', 'create_time', 'modified_time', 'order_number', 'pay_fee']

    def validate(self, attrs):
        # if not self.instance:
        #     chart_ids = attrs.get('chart_ids')
        #     if not chart_ids:
        #         raise serializers.ValidationError('请传入chart_ids参数')
        #     for chart_id in chart_ids:
        #         if not ShoppingChart.objects.filter(id=chart_id, status='NEW').exists():
        #             raise serializers.ValidationError('无效的chart_id: %s，请检查传入参数' % chart_id)
        #     if attrs.get('coupon_list'):
        #         for coupon_id in attrs['coupon_list']:
        #             if not StudentCoupon.objects.filter(user=self.context['request'].user, id=coupon_id,
        #                                                 status='TO_USE').exists():
        #                 raise serializers.ValidationError('无效的优惠券, coupon_id: %s' % coupon_id)
        #
        #     if Order.objects.filter(user=self.context['request'].user,
        #                             status__in=['TO_PAY', 'TO_CONFIRM']).exists():
        #         raise serializers.ValidationError('有未完成的订单，不能创建新的订单')
        # else:
        #     if self.instance.status == 'CANCELED':
        #         raise serializers.ValidationError('该订单已被取消，不能进行更新任何操作')
        #     if self.instance.status == 'TO_PAY':
        #         if attrs.get('status') == 'CONFIRMED':
        #             raise serializers.ValidationError('用户尚未上传凭证，不能进行确认操作')
        #     if self.instance.status == 'TO_CONFIRM':
        #         if attrs.get('status') == 'CANCELED':
        #             raise serializers.ValidationError('该订单已被支付，在管理员确定前不能取消')
        #     if self.instance.status == 'CONFIRMED':
        #         raise serializers.ValidationError('管理员已确认该订单，不能进行任何更新操作')
        #     if self.instance.status == 'CONFIRM_FAILED':
        #         raise serializers.ValidationError('管理员已确认订单支付认证失败，不能进行任何更新操作')
        return attrs

    def validated_data_additional(self, validated_data, chart_ids, coupon_list, user):
        """对validated_data参数进行补充"""
        standard_fee = sum([item.course_fee for item in ShoppingChart.objects.filter(
            id__in=chart_ids, status='NEW')])
        order_count = Order.objects.all().count()
        order_number = '%s%s%s' % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'), user.id, order_count)
        validated_data['order_number'] = order_number
        validated_data['standard_fee'] = standard_fee + 2000
        validated_data['pay_fee'] = standard_fee + 2000
        validated_data['user'] = user
        if coupon_list:
            # validated_data['coupon_list'] = json.dumps(coupon_list)
            # OrderCouponRelation.objects.bulk_create(**{'coupon'})
            # 计算优惠券费用
            coupon_list_fee = 0
            coupon_list_fee_values = StudentCoupon.objects.filter(user=user, coupon_id__in=coupon_list).values_list(
                'coupon__balance', flat=True)
            for item in coupon_list_fee_values:
                coupon_list_fee += item
            validated_data['pay_fee'] = standard_fee + 2000 - coupon_list_fee if \
                (validated_data['standard_fee'] - coupon_list_fee) >= 0 else 0
        return validated_data

    def create(self, validated_data):
        # coupon_list = validated_data.pop('coupon_list', None)
        chart_ids = validated_data.pop('chart_ids')
        user = self.context['request'].user
        coupon_list = [coupon[0] for coupon in
                       StudentCoupon.objects.filter(user=user.id, status='TO_USE').values_list('coupon_id')]
        validated_data = self.validated_data_additional(validated_data, chart_ids, coupon_list, user)
        order = super().create(validated_data)
        self.additional_order_update(order, coupon_list, chart_ids, user)
        return order

    def additional_order_update(self, order, coupon_list, chart_ids, user):
        """订单创建后，更新与订单相关信息"""
        if coupon_list:
            # 更新优惠券状态
            for coupon_id in coupon_list:
                if StudentCoupon.objects.filter(user=user, coupon_id=coupon_id, status='TO_USE').exists():
                    StudentCoupon.objects.filter(user=user, coupon_id=coupon_id, status='TO_USE').update(
                        status='LOCKED')
                OrderCouponRelation.objects.create(**{'coupon_id': coupon_id, 'order': order, 'remark': '创建了订单'})
        # 创建订单与商品关系
        order_chart = []
        for chart_id in chart_ids:
            order_chart.append(OrderChartRelation(order=order, chart_id=chart_id))
        OrderChartRelation.objects.bulk_create(order_chart)

        # 更新购物车
        ShoppingChart.objects.filter(id__in=chart_ids).update(status='ORDERED')
        # 操作记录
        OperationLog.objects.create(operator=user, operation=1, target=user.id,
                                    ip_address=get_ip_address(self.context['request']),
                                    description='创建了订单')
        # order_auto_notice_message(order=order, user=user)
        if user.student_status in ['NEW', 'PERSONAL_FILE']:
            change_student_status(user.id, 'SUPPLY_ORDER')
        return

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        coupon_list = OrderCouponRelation.objects.filter(order=instance).values_list('coupon', flat=True)
        if instance.status == 'CONFIRMED':
            if coupon_list:
                StudentCoupon.objects.filter(user=instance.user, id__in=list(coupon_list)).update(status='USED')
            if instance.user.student_status == 'SUPPLY_ORDER':
                change_student_status(instance.user_id, 'PAYMENT_CONFIRMED')
        if instance.status == 'CANCELED':
            if coupon_list:
                StudentCoupon.objects.filter(user=instance.user, id__in=list(coupon_list)).update(status='TO_USE')
            if instance.user.student_status == 'SUPPLY_ORDER':
                change_student_status(instance.user_id, 'PERSONAL_FILE')
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        charts = ShoppingChartSerializer(ShoppingChart.objects.filter(orderchartrelation__order=instance),
                                         many=True).data
        data['charts'] = charts
        payment_info = PaymentAccountInfo.objects.filter(payment=instance.payment).first()
        data['payment_info'] = PaymentAccountInfoSerializer(payment_info).data if payment_info else None
        order_payment = OrderPayment.objects.filter(order=instance).last()
        data['order_payed_info'] = OrderPaymentSerializer(order_payment).data if order_payment else None
        data['user'] = {
            'id': instance.user.id,
            'name': instance.user.name
        }
        # sales_man = SalesMan.objects.filter(salesmanuser__user=instance.user).first()
        # data['sales_man'] = {'id': sales_man.id, 'name': sales_man.name} if sales_man else {}
        order_coupons = OrderCouponRelation.objects.filter(order=instance).values('coupon__coupon__balance',
                                                                                  'coupon__coupon__name',
                                                                                  'coupon__coupon_expire_at')
        for coupon in order_coupons:
            coupon['amount'] = coupon.pop('coupon__coupon__balance')
            coupon['name'] = coupon.pop('coupon__coupon__name')
            coupon['expire_time'] = coupon.pop('coupon__coupon_expire_at')
        data['coupon_list'] = order_coupons
        order_additional_list = OrderAdditionalPayment.objects.filter(order=instance)
        replenish_list = order_additional_list.filter(type='REPLENISH')
        refund_list = order_additional_list.filter(type='REFUND')
        data['replenish_list'] = OrderAdditionalPaymentSerializer(replenish_list,
                                                                  many=True).data if replenish_list else []
        data['refund_list'] = OrderAdditionalPaymentSerializer(refund_list,
                                                               many=True).data if refund_list else []
        return data


class SimpleUserOrderSerializer(serializers.ModelSerializer):
    status = VerboseChoiceField(choices=Order.STATUS, required=False)
    chart_ids = serializers.ListField(write_only=True, child=serializers.IntegerField())

    class Meta:
        model = Order
        fields = ['id', 'status', 'remark', 'chart_ids', 'user', 'standard_fee', 'create_time',
                  'modified_time', 'order_number', 'pay_fee']
        read_only_fields = ['id', 'status', 'remark', 'chart_ids', 'user', 'standard_fee', 'create_time',
                            'modified_time', 'order_number', 'pay_fee']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        charts = ShoppingChartSerializer(ShoppingChart.objects.filter(orderchartrelation__order=instance),
                                         many=True).data
        data['charts'] = charts
        payment_info = PaymentAccountInfo.objects.filter(payment=instance.payment).first()
        data['payment_info'] = PaymentAccountInfoSerializer(payment_info).data if payment_info else None
        order_payment = OrderPayment.objects.filter(order=instance).last()
        data['order_payed_info'] = OrderPaymentSerializer(order_payment).data if order_payment else None
        data['user'] = {
            'id': instance.user.id,
            'name': instance.user.name
        }
        order_coupons = OrderCouponRelation.objects.filter(order=instance).values('coupon__coupon__balance',
                                                                                  'coupon__coupon__name',
                                                                                  'coupon__coupon_expire_at')
        for coupon in order_coupons:
            coupon['amount'] = coupon.pop('coupon__coupon__balance')
            coupon['name'] = coupon.pop('coupon__coupon__name')
            coupon['expire_time'] = coupon.pop('coupon__coupon_expire_at')
        data['coupon_list'] = order_coupons
        order_additional_list = OrderAdditionalPayment.objects.filter(order=instance)
        replenish_list = order_additional_list.filter(type='REPLENISH')
        refund_list = order_additional_list.filter(type='REFUND')
        data['replenish_list'] = OrderAdditionalPaymentSerializer(replenish_list,
                                                                  many=True).data if replenish_list else []
        data['refund_list'] = OrderAdditionalPaymentSerializer(refund_list, many=True).data if refund_list else []
        return data


class OrderCourseSerializer(serializers.ModelSerializer):
    """用于用户关联订单的审课"""

    class Meta:
        model = Course
        fields = ['id', 'course_code', 'name', 'max_num', 'credit', 'professor', 'start_time', 'end_time',
                  'create_time', 'address', 'syllabus']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_course = ConfirmCourse.objects.filter(course=instance).first()
        user_course_data = {
            'score': user_course.score,
            'score_grade': user_course.score_grade,
            'reporting_time': user_course.reporting_time,
            'confirm_img': user_course.confirm_img.path if user_course.confirm_img else None,
            'status': {
                'key': user_course.status,
                'verbose': dict(ConfirmCourse.STATUS).get(user_course.status)
            }
        } if user_course else None
        data['confirm_course'] = user_course_data
        return data


class OrderRecordSerializer(serializers.ModelSerializer):
    project1 = ProjectSerializer()
    project2 = ProjectSerializer()
    project3 = ProjectSerializer()
    project4 = ProjectSerializer()

    class Meta:
        model = OrderRecord
        fields = ['id', 'order', 'project1', 'course_num1', 'project2', 'course_num2', 'project3', 'course_num3',
                  'project4', 'course_num4', 'all_amount']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['course_num1']:
            data['project1']['course_number'] = data['course_num1']
            data['project1']['project_column'] = 'project1_id'
        if data['course_num2']:
            data['project2']['course_number'] = data['course_num2']
            data['project2']['project_column'] = 'project2_id'
        if data['course_num3']:
            data['project3']['course_number'] = data['course_num3']
            data['project3']['project_column'] = 'project3_id'
        if data['course_num4']:
            data['project4']['course_number'] = data['course_num4']
            data['project4']['project_column'] = 'project4_id'
        return data


class UserOrderCourseSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'project', 'currency', 'payment', 'create_time', 'status',
                  'course_num', 'standard_fee', 'pay_fee', 'project', 'remark']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_course = Course.objects.filter(usercourse__order=instance, usercourse__user=self.context['request'].user)
        user_course_data = OrderCourseSerializer(user_course, many=True).data if user_course else None
        data['user_course'] = user_course_data
        return data


class OrderPaymentSerializer(serializers.ModelSerializer):
    img = Base64ImageField()

    class Meta:
        model = OrderPayment
        fields = ['id', 'img', 'order', 'amount', 'account_name', 'phone', 'relation', 'remark']

    def validate(self, attrs):
        user = self.context['request'].user
        order = attrs['order']
        if order.user.id != user.id:
            raise serializers.ValidationError('您无权限操作他人的订单')
        if OrderPayment.objects.filter(order=order).exists():
            raise serializers.ValidationError('当前订单已经上传过支付信息')
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        order = validated_data['order']
        order.status = 'TO_CONFIRM'
        # order.currency = validated_data.pop('currency')
        # order.payment = validated_data.pop('payment')
        order.save(update_fields=['status'])
        instance = super().create(validated_data)
        # HistoryFactory.create_record(operator=self.context['request'].user, source=instance.order, key='UPDATE',
        #                              remark='上传了订单支付信息', source_type='ORDER')
        if user.student_status in ['NEW', 'PERSONAL_FILE', 'SUPPLY_ORDER']:
            change_student_status(user.id, 'TO_PAYMENT_CONFIRM')
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['img'] = '%s%s%s' % (DOMAIN, MEDIA_URL, instance.img)
        return data


class ShoppingChartSerializer(serializers.ModelSerializer):
    """购物车"""

    class Meta:
        model = ShoppingChart
        fields = ['id', 'project', 'course_num', 'course_fee']
        read_only_fields = ['course_fee']

    def validate(self, attrs):
        # project = attrs['project']
        # if project.start_date < datetime.date.today():
        #     raise serializers.ValidationError('该项目已经开课了，请选择其他项目。')
        # if project.start_date < datetime.date.today() + datetime.timedelta(7):
        #     raise serializers.ValidationError('该项目马上就要开课了，请选择其他项目。')
        # # attrs['course_fee'] = project_course_fee.course_fee + project.apply_fee
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        # validated_data['user'] = user
        project = validated_data.get('project')
        course_num = validated_data.get('course_num')
        course_num_list = [0, 'one', 'two', 'three', 'four', 'five']
        validated_data['course_fee'] = getattr(project, course_num_list[course_num] + '_course_fee')
        # project_num = Project.objects.filter(project=project).values_list('course_number')
        # instance = ShoppingChart.objects.filter(project=project, user=user, status='NEW').first()
        # if instance:
        #     current_course_num = instance.course_num
        #     instance.course_num = current_course_num + course_num
        #     if instance.course_num > max(project_num)[0]:
        #         raise serializers.ValidationError('项目课程数量最大可选%s门,已选择%s门' % (max(project_num)[0], current_course_num))
        #     course_fee = sum(
        #         ProjectCourseFee.objects.filter(project=project, course_number=instance.course_num).values_list(
        #             'course_fee').filter()[0])
        #     instance.course_fee = course_fee
        #     instance.save()
        # else:
        instance = super().create(validated_data)
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['project'] = ProjectSerializer(instance.project).data
        return data


class OrderAdditionalPaymentSerializer(serializers.ModelSerializer):
    type = VerboseChoiceField(choices=OrderAdditionalPayment.TYPE, required=False)
    refunded_type = VerboseChoiceField(choices=OrderAdditionalPayment.REFUND_TYPE, required=False)
    replenish_type = VerboseChoiceField(choices=OrderAdditionalPayment.REPLENISH_TYPE, required=False)
    status = VerboseChoiceField(choices=OrderAdditionalPayment.STATUS, required=False)
    currency = VerboseChoiceField(choices=OrderAdditionalPayment.CURRENCY, required=False)
    img = Base64ImageField(required=False)
    project = ProjectSerializer(required=False)
    project1 = serializers.IntegerField(required=False)
    project2 = serializers.IntegerField(required=False)
    project3 = serializers.IntegerField(required=False)
    project4 = serializers.IntegerField(required=False)
    course_num1 = serializers.IntegerField(required=False)
    course_num2 = serializers.IntegerField(required=False)
    course_num3 = serializers.IntegerField(required=False)
    course_num4 = serializers.IntegerField(required=False)

    class Meta:
        model = OrderAdditionalPayment
        fields = ['id', 'user', 'type', 'refunded_type', 'replenish_type', 'admin_remark', 'student_remark', 'order',
                  'status', 'amount', 'img', 'modified_time', 'create_time', 'add_order_number', 'project1',
                  'course_num1', 'project2', 'course_num2', 'project3', 'course_num3', 'project4', 'course_num4',
                  'currency', 'project', 'course_num']
        read_only_fields = ['id', 'modified_time', 'status', 'create_time', 'add_order_number']

    def create(self, validated_data):
        order_record_dict = OrderRecord.objects.filter(order=validated_data['order']).order_by(
            '-create_time').values().first()
        order_record_dict.pop('create_time')
        order_record_dict.pop('id')
        project_name = validated_data.get('project_column')
        if project_name:
            order_record_dict[project_name] = order_record_dict[project_name]
            validated_data['project'] = order_record_dict[project_name]
            order_record_dict['course_num' + project_name[7:8]] = validated_data.get('course_num')
        if validated_data.get('type') == 'REPLENISH':
            validated_data['status'] = 'TO_PAY'
            order_record_dict['all_amount'] += validated_data['amount']
            OrderRecord.objects.create(**order_record_dict)
        else:
            validated_data['status'] = 'REFUNDED'
        order_count = OrderAdditionalPayment.objects.all().count()
        add_order_number = '%s%s%s' % (
            datetime.datetime.now().strftime('%Y%m%d%H%M%S'), validated_data['user'].id, order_count)
        validated_data['add_order_number'] = add_order_number
        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('img'):
            data['img'] = DOMAIN + data.get('img')
        return data
