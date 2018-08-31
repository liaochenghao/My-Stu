from django.db import models


class Course(models.Model):
    course_code = models.CharField('课程代码', max_length=30, unique=True)
    name = models.CharField('课程名称', max_length=64)
    credit = models.IntegerField('学分', null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    is_active = models.BooleanField('是否启用', default=True)
    extra = models.CharField('备注信息', max_length=255, null=True)

    class Meta:
        db_table = 'course'
