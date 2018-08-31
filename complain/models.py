from django.db import models


# Create your models here.

class Complain(models.Model):
    title = models.CharField('标题', null=True, max_length=64)
    context = models.CharField('内容', null=True, max_length=255)
    picture = models.CharField('图片', null=True, max_length=64)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'complain'
