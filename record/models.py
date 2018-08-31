from django.db import models

# Create your models here.
from channel.models import Channel
from student.models import StudentInfo
from user_info.models import UserInfo


class ChannelRecord(models.Model):
    """渠道记录表"""
    student_id = models.ForeignKey(StudentInfo, db_column='student_id')
    channel_id = models.ForeignKey(Channel, db_column='channel_id')
    status = models.BooleanField('有效标记', default=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'channel_record'


class RecommendRecord(models.Model):
    """推荐记录表"""
    inviter = models.CharField('推荐人编号', max_length=64)
    invitee = models.CharField('被推荐人编号', max_length=64)
    status = models.BooleanField('是否有效', default=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    extra = models.CharField('备注', max_length=255, blank=True)

    class Meta:
        db_table = 'recommend_record'
