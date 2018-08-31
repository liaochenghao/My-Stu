from django.db import models


class Department(models.Model):
    name = models.CharField('部门名称', max_length=30, blank=True)
    description = models.CharField('部门描述', max_length=50, blank=True)
    leader_id = models.CharField('部门负责人编号', max_length=64, blank=True)
    leader_name = models.CharField('部门负责人名称', max_length=64, blank=True)
    enabled = models.BooleanField('是否启用', default=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'department'


class Role(models.Model):
    name = models.CharField('角色名称', max_length=30, blank=True)
    description = models.CharField('角色描述', max_length=50, blank=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    update_at = models.DateTimeField('更新时间', auto_now=True, null=True)
    enabled = models.BooleanField('是否禁用', default=True)

    class Meta:
        db_table = 'role'


class Menu(models.Model):
    name = models.CharField('视图名称', max_length=30)
    url = models.CharField('视图名称', max_length=100, null=True)
    parent_id = models.IntegerField('父级视图编号', default=0)
    extra = models.CharField('备注信息', max_length=30, blank=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'menu'


class Privilege(models.Model):
    id = models.AutoField('权限编号', primary_key=True)
    role_id = models.ForeignKey(Role, db_column='role_id')
    menu_id = models.ForeignKey(Menu, db_column='menu_id')
    extra = models.CharField('备注', max_length=64, blank=True)
    create_at = models.DateTimeField('创建时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'privilege'


class UserInfo(models.Model):
    username = models.CharField('用户名', max_length=50, unique=True)
    password = models.CharField('密码', max_length=255)
    role_id = models.ForeignKey(Role, db_column='role_id')
    role_name = models.CharField('角色名称', max_length=30, blank=True)
    name = models.CharField('真实姓名', max_length=20, blank=True)
    email = models.CharField('电子邮箱', max_length=64, blank=True)
    phone = models.CharField('手机号码', max_length=15, blank=True)
    sex = models.BooleanField('性别', default=True)
    department_id = models.ForeignKey(Department, db_column='department_id')
    department_name = models.CharField('部门名称', max_length=30, blank=True)
    leader_id = models.IntegerField('上级领导编号', default=-1)
    leader_name = models.CharField('上级领导姓名', max_length=20, blank=True)
    active = models.BooleanField('是否启用', default=True)
    wechat = models.CharField('微信号', max_length=32, blank=True)
    qr_code = models.CharField('二维码', max_length=255, blank=True)
    extra = models.CharField('备注信息', max_length=255, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'user_info'
