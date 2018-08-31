from django.db import models

# Create your models here.
from course.models import Course
from project.models import Project, ProjectCourse


class StudentInfo(models.Model):
    """学生信息"""
    GENDER = (
        ('MALE', '男'),
        ('FEMALE', '女')
    )
    STUDENT_STATUS = (
        ('NEW', '新建用户'),
        ('PERSONAL_FILE', '已建档'),
        ('SUPPLY_ORDER', '已提交订单'),
        ('SIGNED_AGREEMENT', '已签署协议'),
        ('TO_PAYMENT_CONFIRM', '待缴费确认'),
        ('PAYMENT_CONFIRMED', '缴费确认成功'),
        ('COMPLETE_FILE', '填写个人信息'),
        ('UPLOAD_FILE', '上传身份证成绩单'),
        ('TO_CHOOSE_COURSE', '沟通选课'),
        ('UPLOAD_CONFIRM', '上传审课图片'),
        ('CONFIRM_POSTIL', '审课批注'),
        ('PICKUP_COURSE', '确认选课'),
        ('IN_CLASS', '上课中'),
        ('AFTER_SCORE', '已出成绩'),
        ('POSTING', '成绩单邮寄中'),
        ('SWITCHED_COURSE', '已学分转换')
    )
    WECHAT_STATUS = (
        ('DEFAULT', '默认'),
        ('INVALID', '无效'),
        ('VALID', '有效'),
    )
    openid = models.CharField('微信openid', max_length=60, null=True, unique=True)
    name = models.CharField('学生姓名', max_length=30, null=True)
    cschool = models.CharField('当前学校', max_length=30, null=True)
    major = models.CharField('专业', max_length=30, null=True)
    email = models.EmailField('个人邮箱', max_length=30, null=True)
    wechat = models.CharField('微信号', max_length=30, null=True)
    wechat_sign = models.CharField('CC标记', choices=WECHAT_STATUS, max_length=30, default='DEFAULT')
    first_name = models.CharField('英文名', max_length=30, null=True)
    last_name = models.CharField('英文姓', max_length=30, null=True)
    phone = models.CharField('联系手机', max_length=11, null=True)
    gender = models.CharField('性别', choices=GENDER, max_length=30, null=True)
    birth_date = models.DateField('出生日期', null=True)
    school_email = models.EmailField('学校邮箱', max_length=30, null=True)
    id_number = models.CharField('身份证号', max_length=30, unique=True, null=True)
    enrollment_year = models.CharField('入学年份', max_length=30, null=True)
    old_student = models.CharField('是否老学员', max_length=60, default=' ')
    student_number = models.CharField('学生证号', max_length=30, unique=True, null=True)
    gpa = models.FloatField('GPA', null=True)
    cc = models.CharField('销售顾问', max_length=60, null=True)
    cc_sign = models.BooleanField('CC标记', default=False)
    server = models.CharField('学服', max_length=60, null=True)
    qr_code = models.CharField('二维码URL', max_length=255, null=True)
    server_sign = models.BooleanField('学服标记', default=False)
    card_img1 = models.ImageField(upload_to='IDcard1', null=True)
    card_img2 = models.ImageField(upload_to='IDcard2', null=True)
    transcript_img = models.ImageField(upload_to='transcript', null=True)
    intention = models.IntegerField('报名意向', null=True, default=0)
    sign_agreement = models.BooleanField('已签署协议', default=0)
    contact = models.CharField('紧急联系人', max_length=60, null=True)
    contact_relation = models.CharField('紧急联系人关系', max_length=60, null=True)
    contact_wechat = models.CharField('紧急联系人微信', max_length=60, null=True)
    contact_email = models.CharField('紧急联系人邮箱', max_length=60, null=True)
    channel_id = models.IntegerField('渠道ID', null=True)
    channel_name = models.CharField('渠道', max_length=60, null=True)
    student_status = models.CharField(choices=STUDENT_STATUS, default='NEW', max_length=60, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    modified_time = models.DateTimeField('跟进时间', auto_now=True)

    class Meta:
        db_table = 'student_info'
        ordering = ['-create_time']

    @property
    def school_info(self):
        return {
            'cschool': self.cschool,
            'major': self.major,
            'enrollment_year': self.enrollment_year,
            'gpa': self.gpa
        }


class StudentInfoRemark(models.Model):
    """学生信息备注"""
    REMARK_TYPE = (
        ('CC', 'CC'),
        ('SERVER', '学服'),
    )
    user = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
    remark_type = models.CharField(choices=REMARK_TYPE, max_length=32, default='CC')
    remark = models.CharField('备注', max_length=255)
    remark_by = models.CharField('备注人', max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_info_remark'
        ordering = ['-create_time']


class StudentScoreDetail(models.Model):
    """学生成绩邮寄信息"""
    user = models.OneToOneField(StudentInfo)
    country = models.CharField('国家', max_length=60, null=True)
    region = models.CharField('地区', max_length=60, null=True)
    city = models.CharField('城市', max_length=60, null=True)
    address1 = models.CharField('详细地址一', max_length=60, default=None, null=True)
    address2 = models.CharField('详细地址二', max_length=60, default=None, null=True)
    post_code = models.CharField('邮编', max_length=30, null=True)
    recipient = models.CharField('收件人', max_length=30, default=None, null=True)
    recipient_phone = models.CharField('联系电话', max_length=30, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_score_detail'


class StudentAgreement(models.Model):
    """学生协议记录表"""
    user_id = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING, db_column='user_id')
    agreement = models.CharField('学生协议图片', max_length=64, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'student_agreement'
