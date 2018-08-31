from django.db import models
from project.models import Project, ProjectCourse
from student.models import StudentInfo
from course.models import Course
from user_info.models import UserInfo


class Review(models.Model):
    """审课方案表"""
    student = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    student_server = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    remark = models.CharField('备注', max_length=255, null=True)

    class Meta:
        db_table = 'review'


class ReviewCourse(models.Model):
    """审课方案课程表"""
    STATUS = (
        ('SUCCESS', '审课成功'),
        ('FAIL', '审课失败'),
        ('WAIT', '待学服确认'),
        ('WAIT_CERTIFICATE', '等待学生上传凭据'),
    )

    review = models.ForeignKey(Review, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    student_id = models.IntegerField('学生id', null=True)
    school = models.CharField('主办大学', max_length=64, null=True)
    course_code = models.CharField('课程代码', max_length=30)
    course_name = models.CharField('课程名称', max_length=64)
    real_name = models.CharField('课程原名', max_length=64, null=True)
    status = models.CharField('审课状态', choices=STATUS, max_length=32, null=True)
    review_certificate = models.CharField('审课凭据', max_length=64, null=True)
    remark = models.CharField('备注', max_length=255, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'review_course'


class ConfirmCourse(models.Model):
    """确认课程表"""

    STATUS = (
        ('SCORE_WAIT', '待学生确认成绩'),
        ('CONFIRMED', '已确认成绩'),
        ('RECONSIDER', '成绩复议中'),
        ('NOTHING', '成绩未录入'),
    )
    CONVERT_STATUS = (
        ('SUCCESS', '学分转换成功'),
        ('FAIL', '学分转换失败'),
        ('CONVERT_WAIT', '学分正在转换'),
        # ('WAIT_IMAGE', '等待学生上传转学分图片'),
        ('NO_SEND', '未寄出'),
        ('SENT', '已寄出'),
        # ('RECEIVED', '已收件'),
    )

    project_course = models.ForeignKey(ProjectCourse, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    course_code = models.CharField('课程代码', max_length=30)
    course_name = models.CharField('课程名称', max_length=64)
    school = models.CharField('主办大学', max_length=64, null=True)
    status = models.CharField('成绩状态', choices=STATUS, max_length=32, null=True)
    convert_status = models.CharField('转学分状态', choices=CONVERT_STATUS, max_length=32, null=True)
    image = models.CharField('转学分图片', max_length=64, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    remark = models.CharField('备注', max_length=255, null=True)
    score = models.IntegerField('成绩分数', null=True)
    score_enter_time = models.DateTimeField('成绩录入时间', null=True)
    grade = models.CharField('等级', max_length=16, null=True)
    recipient_number = models.CharField('快递单号', max_length=60, null=True)
    sending_date = models.DateField('寄送日期')

    class Meta:
        db_table = 'confirm_course'


class ChangeCourseRecord(models.Model):
    """学生调课记录表"""
    student = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    student_server = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    course_code = models.CharField('课程编号', max_length=32, null=True)
    course_name = models.CharField('课程名称', max_length=32, null=True)
    school = models.CharField('主办大学', max_length=64, null=True)
    project = models.CharField('课程关联项目名称', max_length=64, null=True)
    course = models.CharField('原课程名称', max_length=32, null=True)
    change_type = models.CharField('调整类别', max_length=16, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    extra = models.CharField('备注', max_length=255, null=True)

    class Meta:
        db_table = 'change_course_record'
