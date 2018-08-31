from django.db import models


class Common(models.Model):
    """
    公共信息表
    """
    context = models.CharField('成绩公示信息', max_length=255, null=True)
    extra1 = models.CharField("备用", max_length=255, null=True)
    extra2 = models.CharField("备用", max_length=255, null=True)
    extra3 = models.CharField("备用", max_length=255, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = "common"
