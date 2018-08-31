from django.db import models

# Create your models here.
from student.models import StudentInfo
from user_info.models import UserInfo


class Coupon(models.Model):
    COUPON_TYPE = (
        (1, '阶段优惠'),
        (2, '特殊优惠'),
        (3, '老学员优惠'),
    )
    code = models.CharField('优惠券码', null=True, max_length=30)
    name = models.CharField('优惠券名称', null=True, max_length=30)
    balance = models.IntegerField('优惠券金额')
    start_at = models.DateTimeField('优惠券开始时间')
    end_at = models.DateTimeField('优惠券截止时间')
    type = models.IntegerField('优惠券类型', choices=COUPON_TYPE)
    total = models.IntegerField('优惠券数量', default=-1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'coupon'


class StudentCoupon(models.Model):
    STATUS = (
        ('TO_USE', '未使用'),
        ('LOCKED', '被锁定'),
        ('USED', '已使用')
    )
    user = models.ForeignKey(StudentInfo, db_column='user_id')
    coupon = models.ForeignKey(Coupon, db_column='coupon_id')
    status = models.CharField(max_length=30, choices=STATUS, default='TO_USE')
    coupon_expire_at = models.DateTimeField('优惠券过期时间')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'student_coupon'
