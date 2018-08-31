# coding: utf-8

import random
from urllib import parse
import qrcode
from record.models import ChannelRecord, RecommendRecord
from student.models import StudentInfo
from StudentManageSys.settings import DOMAIN, MEDIA_URL, WX_CONFIG, MEDIA_ROOT
from user_info.models import UserInfo


def change_student_status(student_id, status):
    student_instance = StudentInfo.objects.filter(id=student_id).update(student_status=status)
    # student_instance.student_status = status
    # student_instance.save()
    return


def make_qrcode(student_id):
    redirect_uri = parse.quote('%s/?student_id=%s' % (DOMAIN, student_id))
    student_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_base&state=STATE#wechat_redirect' % (
        WX_CONFIG['APP_ID'], redirect_uri)
    student_img = qrcode.make(student_url)
    qr_code_save_path = '%s%s%s%s' % (MEDIA_ROOT, '/images/user_qrcode/', student_id, '.jpg')
    qr_code_url = '%s%s%s%s%s' % (DOMAIN, MEDIA_URL, 'images/user_qrcode/', student_id, '.jpg')
    student_img.save(qr_code_save_path)
    return (qr_code_url, student_url)


def auto_assign_sales_man(user):
    """
    自动分配销售顾问，
    如果该用户存在推荐给他的用户(A)，则将推荐给他人(A)的销售顾问分配给该用户。
    如果用户进入时存在渠道信息，则将该渠道的销售人员直接分配给该用户。
    :param user:
    :return:
    """
    sales_man_all = UserInfo.objects.filter(department_id=1)
    if not sales_man_all:
        return dict()
    if not user.cc:
        channel = ChannelRecord.objects.filter(user_id=user.id).order_by('-create_time').values(
            'channel_id__sales_man_id').first()
        recommend_user = RecommendRecord.objects.filter(invitee=user.id).order_by('-create_time').first()

        if recommend_user:
            # 如果该用户存在推荐给他的用户(A)
            recommend_user_salesman = StudentInfo.objects.filter(id=recommend_user.inviter).first()
            if recommend_user_salesman:
                sales_man = recommend_user_salesman.cc
            else:
                rand_int = random.randint(1, len(sales_man_all))
                sales_man = sales_man_all[rand_int - 1].id
        elif channel:
            # 如果用户进入时存在渠道信息
            sales_man = channel.get('channel_id__sales_man_id')
        else:
            rand_int = random.randint(1, len(sales_man_all))
            sales_man = sales_man_all[rand_int - 1].id

        # if DOMAIN in sales_man.qr_code.path:
        #     qr_code = sales_man.qr_code.path
        # else:
        #     qr_code = '%s%s%s' % (DOMAIN, MEDIA_URL, str(sales_man.qr_code))
        # SalesManUser.objects.create(user=user, sales_man=sales_man)
        # instance = StudentInfo.objects.filter(user=user).first()
        user.cc = sales_man
        user.save()
        res = sales_man
    else:
        # res = SalesMan.objects.filter(salesmanuser__user=user).values('id', 'name', 'email', 'qr_code', 'wechat')[0]
        # res['qr_code'] = '%s%s%s' % (DOMAIN, MEDIA_URL, res['qr_code'])
        res = user.cc
    return res
