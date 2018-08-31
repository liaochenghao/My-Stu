from django.db import models


class Campus(models.Model):
    """
    校区信息表
    """
    name = models.CharField('校区名称', max_length=30, unique=True)
    info = models.CharField("校区描述", max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)
    is_active = models.BooleanField('是否启用', default=True)

    class Meta:
        db_table = "campus"
