from django.db import models


# Create your models here.
from user_info.models import UserInfo


class Channel(models.Model):
    """推广渠道"""
    name = models.CharField('推广名称', unique=True, max_length=30)
    sales_man = models.ForeignKey(UserInfo)
    plan_date = models.DateField('计划推广日期')
    plan_student_number = models.IntegerField('预计参加人数')
    plan_file_student_number = models.IntegerField('预计建档人数')
    plan_payed_student_number = models.IntegerField('预计缴费人数')
    phase_discount = models.CharField('阶段优惠说明', max_length=60, null=True)
    channel_url = models.CharField('推广二维码URL', max_length=255, null=True)
    qr_code = models.ImageField('推广二维码', max_length=64, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'channel'
