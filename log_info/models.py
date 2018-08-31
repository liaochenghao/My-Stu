from django.db import models

# Create your models here.
from user_info.models import UserInfo


class OperationLog(models.Model):
    operator = models.CharField('操作人编号', max_length=64, db_index=True)
    operation = models.IntegerField('操作类型')
    target = models.CharField('操作对象ID', blank=True, max_length=64)
    ip_address = models.GenericIPAddressField('操作人IP地址')
    description = models.CharField('描述', max_length=255, blank=True)
    operator_type = models.IntegerField('操作人类型', default=0)
    create_time = models.DateTimeField('操作时间', auto_now_add=True, null=True)

    class Meta:
        db_table = 'operation_log'
