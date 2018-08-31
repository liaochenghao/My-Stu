from django.db import models

# coding: utf-8
from project.models import Project
from coupon.models import StudentCoupon
from django.db import models

from student.models import StudentInfo, StudentScoreDetail


class ShoppingChart(models.Model):
    """购物车"""
    STATUS = (
        ('NEW', '新添加'),
        ('ORDERED', '已下单'),
        ('PAYED', '已支付'),
        ('DELETED', '已删除')
    )
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    course_num = models.IntegerField('课程数量')
    course_fee = models.FloatField('课程费用')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('状态', max_length=30, choices=STATUS, default='NEW')

    class Meta:
        db_table = 'shopping_chart'


class Order(models.Model):
    """订单"""
    CURRENCY = (
        ('FOREIGN_CURRENCY', '外币'),
        ('RMB', '人民币')
    )
    PAYMENT = (
        ('BANK', '银行转账'),
        ('ALI_PAY', '支付宝转账'),
        ('PAY_PAL', 'PAY_PAL支付'),
        ('OFF_LINE', '面付')
    )
    STATUS = (
        ('CANCELED', '已取消'),
        ('TO_PAY', '待支付'),
        ('TO_CONFIRM', '待确认'),
        ('CONFIRMED', '已确认'),
        ('CONFIRM_FAILED', '验证失败')
    )
    user = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    order_number = models.CharField('订单号', max_length=30, null=True, unique=True)
    currency = models.CharField('币种', choices=CURRENCY, max_length=30, null=True)
    payment = models.CharField('支付方式', choices=PAYMENT, max_length=30, null=True)
    status = models.CharField('订单状态', choices=STATUS, max_length=30, default='TO_PAY')
    standard_fee = models.FloatField('标准费用')
    pay_fee = models.FloatField('支付费用', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    remark = models.CharField('订单备注', max_length=255, null=True)

    class Meta:
        db_table = 'order'


class OrderRecord(models.Model):
    """最终订单记录"""
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    project1 = models.ForeignKey(Project, related_name='project1', on_delete=models.DO_NOTHING)
    course_num1 = models.IntegerField('课程数量1')
    project2 = models.ForeignKey(Project, related_name='project2', on_delete=models.DO_NOTHING, null=True)
    course_num2 = models.IntegerField('课程数量2', null=True)
    project3 = models.ForeignKey(Project, related_name='project3', on_delete=models.DO_NOTHING, null=True)
    course_num3 = models.IntegerField('课程数量3', null=True)
    project4 = models.ForeignKey(Project, related_name='project4', on_delete=models.DO_NOTHING, null=True)
    course_num4 = models.IntegerField('课程数量4', null=True)
    all_amount = models.FloatField('总费用')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_record'


class OrderChartRelation(models.Model):
    """订单与商品关系"""
    chart = models.ForeignKey(ShoppingChart, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_chart_relation'


class OrderCouponRelation(models.Model):
    """订单与优惠券关系"""
    coupon = models.ForeignKey(StudentCoupon, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    remark = models.CharField('备注', max_length=255, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_coupon_relation'


class OrderPayment(models.Model):
    """订单支付信息"""
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    amount = models.FloatField('支付金额')
    img = models.ImageField(upload_to='order')
    account_name = models.CharField('汇款人姓名', max_length=60)
    phone = models.CharField('汇款人电话', max_length=60)
    relation = models.CharField('关系', max_length=60)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_payment'


class OrderAdditionalPayment(models.Model):
    """订单补缴/退费信息"""
    TYPE = (
        ('REPLENISH', '补缴'),
        ('REFUND', '退费'),
    )
    REFUND_TYPE = (
        ('CONFIRM_FAILED', '常规原因(审课失败)'),
        ('PERSONAL_REASONS', '常规原因(个人原因)'),
        ('MORE_TUITION', '常规原因(学费多交)'),
        ('PROJECT_CHANGE1', '项目调整(正常)'),
        ('PROJECT_CHANGE2', '项目调整(面转网)'),
    )
    REPLENISH_TYPE = (
        ('ADD_COURSE', '加课'),
        ('ADD_TRANSCRIPT', '成绩单附加费'),
        ('REPAIR_COURSE', '补齐课程费'),
        ('REPAIR_TUITION', '补齐学费'),
        ('PROJECT_CHANGE1', '项目调整(正常)'),
        ('PROJECT_CHANGE2', '项目调整(面转网)'),
    )
    CURRENCY = (
        ('FOREIGN_CURRENCY', '外币'),
        ('RMB', '人民币')
    )
    STATUS = (
        ('CANCELED', '已取消'),
        ('TO_PAY', '待支付'),
        ('TO_CONFIRM', '待确认'),
        ('CONFIRMED', '已确认'),
        ('CONFIRM_FAILED', '验证失败'),
        ('REFUNDED', '已退款'),
    )
    add_order_number = models.CharField('订单号', max_length=30, null=True, unique=True)
    user = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    type = models.CharField('类型', choices=TYPE, max_length=30)
    amount = models.FloatField('金额')
    course_num = models.IntegerField('课程数量', null=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, null=True)
    img = models.ImageField(upload_to='order', null=True)
    currency = models.CharField('币种', choices=CURRENCY, max_length=30, null=True)
    replenish_type = models.CharField('补缴类型', choices=REPLENISH_TYPE, max_length=30, null=True)
    refunded_type = models.CharField('退费类型', choices=REFUND_TYPE, max_length=30, null=True)
    status = models.CharField('状态', choices=STATUS, max_length=30, null=True)
    admin_remark = models.CharField(max_length=255, blank=True, null=True)
    student_remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_additional_payment'
