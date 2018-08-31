from django.db import models

from campus.models import Campus
from course.models import Course


class Project(models.Model):
    """项目表"""
    campus = models.ForeignKey(Campus, on_delete=models.DO_NOTHING)
    campus_name = models.CharField('关联校区名称', max_length=64, null=True)
    name = models.CharField('项目名称', max_length=30, null=True)
    start_date = models.DateField('开始时间')
    end_date = models.DateField('结束时间')
    address = models.CharField('项目地点', max_length=100, null=True)
    info = models.CharField('项目描述', max_length=255, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    apply_fee = models.FloatField('申请费', null=True)
    course_num = models.IntegerField('课程数')
    one_course_fee = models.FloatField('一门课程的费用', null=True)
    two_course_fee = models.FloatField('两门课程的费用', null=True)
    three_course_fee = models.FloatField('三门课程的费用', null=True)
    four_course_fee = models.FloatField('四门课程的费用', null=True)
    five_course_fee = models.FloatField('五门课程的费用', null=True)
    is_active = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = 'project'


class ProjectCourse(models.Model):
    """项目课程关联表"""
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    campus_id = models.IntegerField('校区id', null=True)
    course_name = models.CharField('课程别名', max_length=64)
    course_code = models.CharField('课程代码', max_length=30, null=True)
    professor = models.CharField('授课教授', max_length=30)
    max_select_num = models.IntegerField('最大选课人数')
    start_time = models.DateField('上课开始时间')
    end_time = models.DateField('上课结束时间')
    address = models.CharField('上课地点', max_length=100)
    status = models.BooleanField('是否删除', default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'project_course'
