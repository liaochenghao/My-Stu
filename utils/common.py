# coding: utf-8
import datetime
import logging
from StudentManageSys.settings import DOMAIN
from log_info.models import OperationLog

logger = logging.getLogger('django')


def append_url_with_domain(url):
    """
    对静态资源文件路径进行拼接，返回服务器上资源地址
    :param url: eg: images/head/123.jpg
    :return: eg: https://cp1.lxhelper.com/media/images/head/123.jpg
    """
    if not url:
        return ''
    return DOMAIN + '/media/' + str(url)


def get_ip_address(request):
    """
    从用户请求中获取访问IP地址
    :param request:
    :return:
    """
    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']


def log_to_db(**kwargs):
    """
    :param kwargs: operator 操作人编号
    :param kwargs: operation 操作类型
    :param kwargs: target 操作对象
    :param kwargs: ip_address IP地址
    :param kwargs: description 描述备注
    :return:
    """
    OperationLog.objects.create(**kwargs)


def datetime_format(data_time):
    """
    将时间进行格式化
    :param data_time:
    :return:
    """
    return datetime.datetime.strptime(data_time.replace('T', ' ')[:-7], "%Y-%m-%d %H:%M:%S")
