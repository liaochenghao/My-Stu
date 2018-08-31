from django.db import models

# Create your models here.
from student.models import StudentInfo


class StudentMessage(models.Model):
    """学生消息记录表"""

    student = models.ForeignKey(StudentInfo)
    message = models.CharField('消息内容', max_length=255, null=True)
    status = models.BooleanField('是否已读', default=False)
    type = models.IntegerField('消息类型', default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student_message'
